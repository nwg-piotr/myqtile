#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from libqtile import bar, widget

soft_sep = {'linewidth': 2, 'size_percent': 70, 'foreground': '393939', 'padding': 7}

# We'll define top and bottom bars for up to 4 displays. Add more if needed.

primary_top = bar.Bar(
    [
        widget.CurrentLayoutIcon(scale=0.5, foreground="EFEFEF", ),
        widget.GroupBox(inactive="999999"),
        widget.Sep(linewidth=2, size_percent=100, padding=12),
        widget.Prompt(),
        widget.TaskList(),
        widget.Pacman(),
        widget.Systray(),
        widget.Sep(**soft_sep),
        widget.Clock(format='%Y-%m-%d %a %H:%M:%S'),
        # widget.Battery(format='{char} {percent:2.0%}'),
    ], 30)

primary_bottom = bar.Bar(
    [
        widget.Net(interface="enp5s0"),
        widget.Spacer(),
        widget.Mpris2(name='audacious', objname='org.mpris.MediaPlayer2.audacious'),
        widget.Memory(fmt='{MemUsed}/{MemTotal}MB'),
        widget.DF(visible_on_warn=False),
        widget.Sep(**soft_sep),
        widget.Volume(),
        widget.Sep(**soft_sep),
        # This widget may crash qtile if a thermal sensor not found
        # widget.ThermalSensor(),
        widget.Sep(**soft_sep),
        widget.Memory(),
    ], 30)

secondary_top = bar.Bar(
    [
        widget.CurrentLayoutIcon(scale=0.5, foreground="EFEFEF", ),
        widget.GroupBox(inactive="999999"),
        widget.Sep(linewidth=2, size_percent=100, padding=12),
        widget.Prompt(),
        widget.TaskList(),
    ], 30)

secondary_bottom = None

tertiary_top = bar.Bar(
    [
        widget.CurrentLayoutIcon(scale=0.5, foreground="EFEFEF", ),
        widget.GroupBox(inactive="999999"),
        widget.Sep(linewidth=2, size_percent=100, padding=12),
        widget.Prompt(),
        widget.TaskList(),
    ], 30)

tertiary_bottom = None

quaternary_top = bar.Bar(
    [
        widget.CurrentLayoutIcon(scale=0.5, foreground="EFEFEF", ),
        widget.GroupBox(inactive="999999"),
        widget.Sep(linewidth=2, size_percent=100, padding=12),
        widget.Prompt(),
        widget.TaskList(),
    ], 30)

quaternary_bottom = None
