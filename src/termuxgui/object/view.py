from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg

class View:
    
    def __init__(self, activity, id):
        self.a = activity
        self.id = id
        if self.id == -1:
            raise RuntimeError("Could not create View")
    
    def deleteview(self):
        __send_msg(self.a.c._main, dumps({"method": "deleteView", "params": {"aid": self.a.aid, "id": self.id}}))
    
    def setmargin(self, margin, dir=None):
        args = {"aid": self.a.aid, "id": self.id, "margin": margin}
        if dir != None:
            args["dir"] = dir
        __send_msg(self.a.c._main, dumps({"method": "setMargin", "params": args}))
    
    def setwidth(self, width):
        __send_msg(self.a.c._main, dumps({"method": "setWidth", "params": {"aid": self.a.aid, "id": self.id, "width": width}}))

    def setheight(self, height):
        __send_msg(self.a.c._main, dumps({"method": "setHeight", "params": {"aid": self.a.aid, "id": self.id, "height": height}}))
    
    def setdimensions(self, width, height):
        self.setwidth(width)
        self.setheight(height)
    
    def setlinearlayoutparams(self, weight):
        __send_msg(self.a.c._main, dumps({"method": "setLinearLayoutParams", "params": {"aid": self.a.aid, "id": self.id, "weight": weight}}))
    
    
    
    def handleevent(self, e):
        pass
    
    
    
    
    
    
