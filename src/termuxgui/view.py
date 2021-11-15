from json import dumps


class View:

    def __init__(self, activity, id):
        self.a = activity
        self.id = id
        if self.id == -1:
            raise RuntimeError("Could not create View")
    
    def __eq__(self, other):
        if type(other) is int:
            return self.id == other
        if isinstance(other, View):
            return self.id == other.id
    
    def deleteview(self):
        self.a.c.send_msg({"method": "deleteView", "params": {"aid": self.a.aid, "id": self.id}})

    def setmargin(self, margin, dir=None):
        args = {"aid": self.a.aid, "id": self.id, "margin": margin}
        if dir != None:
            args["dir"] = dir
        self.a.c.send_msg({"method": "setMargin", "params": args})

    def setwidth(self, width):
        self.a.c.send_msg({"method": "setWidth", "params": {"aid": self.a.aid, "id": self.id, "width": width}})

    def setheight(self, height):
        self.a.c.send_msg({"method": "setHeight", "params": {"aid": self.a.aid, "id": self.id, "height": height}})

    def setdimensions(self, width, height):
        self.a.setwidth(width)
        self.a.setheight(height)

    def setlinearlayoutparams(self, weight):
        self.a.c.send_msg({"method": "setLinearLayoutParams", "params": {"aid": self.a.aid, "id": self.id, "weight": weight}})



    def handleevent(self, e):
        pass






