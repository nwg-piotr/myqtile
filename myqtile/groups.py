#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import common
from libqtile.config import Group, ScratchPad, DropDown

common.num_screens = common.count_displays()

groups = []
groups.extend([
    Group("1: ", spawn="", layout="columns", persist=True),
    Group("2: ", spawn="chromium", layout="columns", persist=True),
    Group("3: ", spawn="", layout="columns", persist=True),
    Group("4: ", spawn="", layout="max", persist=True),
    Group("5: ", spawn="", layout="stack", persist=True),
    Group("6: ", spawn="", layout="columns", persist=True),
    Group("7: ", spawn="", layout="columns", persist=True),
    Group("8: ", spawn="", layout="columns", persist=True)
])

# Scratchpad
groups.append(
    ScratchPad("scratchpad", [
        # Originally it was urxvt terminal here, but I prefer having media player in the scratchpad
        DropDown("player", "audacious", opacity=0.9, width=0.7, height=0.7, on_focus_lost_hide=False),
    ]),
)
