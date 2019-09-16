#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import common

from libqtile.config import Key, Drag, Click
from libqtile.command import lazy

from groups import groups

mod = "mod4"
mod1 = "mod1"
rofr = os.path.join(os.getenv('HOME'), ".config/qtile/rofr.sh")


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod], "Tab", lazy.layout.down()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "h", lazy.layout.next()),
    Key([mod], "l", lazy.layout.next()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Resize
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod], "n", lazy.layout.normalize()),

    # Close window
    Key([mod1], "q", lazy.window.kill()),

    # Swap panes of split stack
    # Key([mod, "shift"], "space", lazy.layout.rotate()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Run applications
    Key([mod], "Return", lazy.spawn("tilix")),
    Key([mod], "t", lazy.spawn("tilix")),
    Key([mod], "w", lazy.spawn("chromium")),
    Key([mod], "e", lazy.spawn("mousepad")),
    Key([mod], "f", lazy.spawn("caja")),
    Key([mod], "c", lazy.spawn("azote")),

    # Let's use a copy of the original ArchLabs script, due to the different logout command
    Key([mod1], "F1", lazy.spawn(os.path.join(rofr + ' -r'))),
    Key([mod], "x", lazy.spawn(os.path.join(rofr + ' -l'))),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod, "shift"], "e", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # toggle visibility of above defined DropDown named "player"
    Key([mod], 'z', lazy.group['scratchpad'].dropdown_toggle('player')),

    # Key bindings below use obhud (https://github.com/nwg-piotr/obhud) commands. Install obhud from AUR or redefine.

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("obhud --volume up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("obhud --volume down")),
    Key([], "XF86AudioMute", lazy.spawn("obhud --volume toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("obhud --brightness up")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("obhud --brightness down")),

    # Touchpad
    Key([], "XF86TouchpadToggle", lazy.spawn("obhud --touchpad toggle")),
]


# Depending on how many screens detected, we may need to assign groups to them differently. Adjust to your needs.
# k is the key/group
# g is which screen it should go on
k = ["1", "2", "3", "4", "5", "6", "7", "8", "equal"]

if common.num_screens == 4:
    g = [0, 0, 1, 1, 2, 2, 3, 3, 0]
elif common.num_screens == 3:
    g = [0, 0, 0, 0, 1, 1, 2, 2, 0]
elif common.num_screens == 2:
    g = [0, 0, 0, 0, 1, 1, 1, 1, 0]
else:
    g = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Loop over the groups, and setup keys for each group to move groups to screens and move focus to screens/groups
for index, i in enumerate(groups):
    keys.extend([
        # mod + number of group (starting with 1) = switch to group
        Key([mod], k[index],
            lazy.group[i.name].toscreen(g[index]),
            lazy.to_screen(g[index])),

        # mod + shift + number of group (starting with 1) = switch to & move focused window to group
        Key([mod, "shift"], k[index], lazy.window.togroup(i.name)),
    ])

# Drag floating layouts todo learn why the hell it does not work
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
