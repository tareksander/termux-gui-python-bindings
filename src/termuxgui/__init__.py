__all__ = ["activity", "bringtasktofront", "connect", "create", "event", "finishactivity", 
"finishtask", "setinputmode", "setpipparams", "settaskdescription", "settheme", "totermux", "viewactions"]

for m in __all__:
    exec("from termuxgui."+m+" import *")
del m

