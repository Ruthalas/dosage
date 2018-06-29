# -*- coding: utf-8 -*-
# Imported from: https://github.com/pycontribs/tendo
# License: PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
# Author: Sorin Sbarnea
# Changes: Modified to be a context manager, use dosage logging

from __future__ import absolute_import, division, print_function

import errno
import os
import sys
import tempfile

from .output import out
from . import AppName

try:
    import fcntl
except ImportError:
    fcntl = None


class SingleInstanceException(BaseException):
    pass


def SingleInstance(basepath=sys.argv[0], exit_code=-1):
    if sys.platform == 'win32':
        return SingleInstanceWin32(basepath, exit_code)
    else:
        return SingleInstanceUnix(basepath, exit_code)


class SingleInstanceBase(object):
    def __init__(self, basepath, exit_code):
        basename = AppName + os.path.realpath(basepath).replace(
            "/", "-").replace(":", "").replace("\\", "-") + '.lock'
        self.lockfile = os.path.normpath(
            os.path.join(tempfile.gettempdir(), basename))
        self.exit_code = exit_code

        out.debug("SingleInstance lockfile: " + self.lockfile)

    def exit(self):
        """Exit with an error message and the given exit code."""
        out.error("Another instance is already running, quitting.")
        if self.exit_code is not None:
            sys.exit(self.exit_code)
        else:
            raise SingleInstanceException()


class SingleInstanceWin32(SingleInstanceBase):
    def __enter__(self):
        try:
            # file already exists, we try to remove (in case previous
            # execution was interrupted)
            if os.path.exists(self.lockfile):
                os.unlink(self.lockfile)
            self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
        except OSError:
            type, e, tb = sys.exc_info()
            if e.errno == errno.EACCES:  # EACCES == 13
                self.exit()
            raise
        return self

    def __exit__(self, *exc):
        os.close(self.fd)
        os.unlink(self.lockfile)
        return False


class SingleInstanceUnix(SingleInstanceBase):
    def __enter__(self):
        self.fp = open(self.lockfile, 'w')
        self.fp.flush()
        try:
            fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            # raises IOError on Python << 3.3, else OSError
        except (IOError, OSError):
            self.exit()
        return self

    def __exit__(self, *exc):
        fcntl.lockf(self.fp, fcntl.LOCK_UN)
        self.fp.close()
        if os.path.isfile(self.lockfile):
            os.unlink(self.lockfile)
        return False
