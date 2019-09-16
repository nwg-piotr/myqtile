#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import common
from libqtile.config import Screen

from bars import *

screens = [Screen(top=primary_top, bottom=primary_bottom)]

# Add as many displays as detected (up to 4, add more if needed - here and in bars.py)
if common.num_screens == 2:
    screens.append(Screen(top=secondary_top, bottom=secondary_bottom))

if common.num_screens == 3:
    screens.append(Screen(top=tertiary_top, bottom=tertiary_bottom))

if common.num_screens == 4:
    screens.append(Screen(top=quaternary_top, bottom=quaternary_bottom))
