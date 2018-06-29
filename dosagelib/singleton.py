# -*- coding: utf-8 -*-
# Copied from: https://github.com/pycontribs/tendo
# License: PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
# Author: Sorin Sbarnea
# Changes: changed logging and formatting

from __future__ import absolute_import, division, print_function

import errno
import os
import sys
import tempfile
from .output import out


class SingleInstanceException(BaseException):
    pass


class SingleInstance(object):
    def __init__(self, flavor_id="", exit_code=-1):
        self.initialized = False
        basename = os.path.splitext(os.path.realpath(sys.argv[0]))[0].replace(
            "/", "-").replace(":", "").replace("\\", "-")
        if flavor_id:
            basename += "-%s" % flavor_id
        basename += '.lock'
        self.lockfile = os.path.normpath(
            os.path.join(tempfile.gettempdir(), basename))

        out.debug("SingleInstance lockfile: " + self.lockfile)
        if sys.platform == 'win32':
            try:
                # file already exists, we try to remove (in case previous
                # execution was interrupted)
                if os.path.exists(self.lockfile):
                    os.unlink(self.lockfile)
                self.fd = os.open(
                    self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            except OSError:
                type, e, tb = sys.exc_info()
                if e.errno == errno.EACCES:  # EACCES == 13
                    self.exit(exit_code)
                raise
        else:  # non Windows
            import fcntl
            self.fp = open(self.lockfile, 'w')
            self.fp.flush()
            try:
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
                # raises IOError on Python << 3.3, else OSError
            except (IOError, OSError):
                self.exit(exit_code)
        self.initialized = True

    def exit(self, exit_code):
        """Exit with an error message and the given exit code."""
        out.error("Another instance is already running, quitting.")
        if exit_code is not None:
            sys.exit(exit_code)
        else:
            raise SingleInstanceException()

    def __del__(self):
        """Remove the lock file."""
        if not self.initialized:
            return
        try:
            if sys.platform == 'win32':
                if hasattr(self, 'fd'):
                    os.close(self.fd)
                    os.unlink(self.lockfile)
            else:
                import fcntl
                fcntl.lockf(self.fp, fcntl.LOCK_UN)
                os.close(self.fp)
                if os.path.isfile(self.lockfile):
                    os.unlink(self.lockfile)
        except Exception as e:
            out.exception("could not remove lockfile: %s" % e)
