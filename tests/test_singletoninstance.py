# -*- coding: utf-8 -*-
# Imported from: https://github.com/pycontribs/tendo
# License: PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
# Author: Sorin Sbarnea
# Changes: Modified to be a context manager, use dosage logging

from __future__ import absolute_import, division, print_function

import time
from multiprocessing import Process

from dosagelib import singleton


def f(basepath):
    with singleton.SingleInstance(basepath=basepath, exit_code=1):
        time.sleep(0.05)


class TestSingleton(object):
    def test_1(self):
        # test in current process
        with singleton.SingleInstance(basepath="test-1"):
            pass
        assert True

    def test_2(self):
        # test in current subprocess
        p = Process(target=f, args=("test-2",))
        p.start()
        p.join()
        # the called function should succeed
        assert p.exitcode == 0

    def test_3(self):
        # test in current process and subprocess with failure
        # start first instance
        with singleton.SingleInstance(basepath="test-3"):
            # second instance
            p = Process(target=f, args=("test-3",))
            p.start()
            p.join()
            assert p.exitcode != 0
            # third instance
            p = Process(target=f, args=("test-3",))
            p.start()
            p.join()
            assert p.exitcode != 0
