# myqtile

This config is a modification of the https://github.com/qtile/qtile-examples/tree/master/oboingo example. 
The main change is that it does not use multi-headed setups predefined for certain host names.
It uses xrandr instead, to detect the number of currently connected displays, and displaces 8 groups (workspaces)
on up to 4 screens. It would be easy to add more if needed.

Other adjustments (group names, key bindings) in majority come from default ArchLabs configs, which I'm used to.

I also added a copy of the ArchLabs `rofr.sh` script. The logout command has been adjusted to qtile.

DO NOT FORGET to edit `autostart.sh` to your needs / installed packages.

DO NOT DELETE the `__init__.py` file.

## Known issues

- after starting qtile, you need to use (`[mod, "control"], "r"`) for the config to work on all displays;
- Dragging floating layouts does not work as expected.
