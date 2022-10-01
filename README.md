# Termux:GUI Python Bindings
A Python library to interact with the Termux:GUI plugin.  
  
See [here](https://github.com/tareksander/termux-gui-python-bindings/blob/main/TUTORIAL.md) for a tutorial
and [here](https://github.com/tareksander/termux-gui-python-bindings/blob/main/TUTORIAL_OOP.md) for using the more object-oriented subpackage.  
  
There is also [documentation](https://tareksander.github.io/termux-gui-python-bindings/index.html) generated from the docstrings.   


### Installing and updating:  
Just use `pip install termuxgui` to install from pypi.


### Usage in `proot-distro`

Set the environment variable `TGUI_PY_UID` to the Termux UID (you can get that using `echo $UID` in a normal Termux shell).  
This gives a warning that the UID the library uses to check the connection is not the UID of the running program.  
Set `TGUI_PY_UID_NOWARN` to any value to suppress this warning.


### License

The license is the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).  
TL;DR: You can use this library in your own projects, regardless of the license you choose for it. Modifications to this library have to be published under the MPL 2.0 (or a GNU license in some cases) though.
