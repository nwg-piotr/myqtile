#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import subprocess

num_screens = 1


def count_displays():
    """
    Checking number of displays depends on the xrandr command!
    :return: Number of detected displays
    """
    return len(
        subprocess.check_output("xrandr | awk '/ connected/{print $1}'", shell=True).decode("utf-8").splitlines())
