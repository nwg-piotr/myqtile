#!/bin/sh
nm-applet &
xrandr --auto --output HDMI1 --mode 1920x1080 --rate 60 --right-of eDP1 &
lxpolkit &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
compton  &
flameshot &
# pressing super key alone simulates pressing Alt-F1
ksuperkey -e 'Super_L=Alt_L|F1' &
ksuperkey -e 'Super_R=Alt_L|F1' &
~/.fehbg
obhud --touchpad off &
light -S 20 &
numlockx on &
