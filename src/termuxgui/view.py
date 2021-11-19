from json import dumps


class View:
    """This represents a generic View."""
    
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
    
    def delete(self):
        """Deletes this View from the layout."""
        self.a.c.send_msg({"method": "deleteView", "params": {"aid": self.a.aid, "id": self.id}})

    def setmargin(self, margin, dir=None):
        """Sets the margins of this View for one or all directions."""
        args = {"aid": self.a.aid, "id": self.id, "margin": margin}
        if dir != None:
            args["dir"] = dir
        self.a.c.send_msg({"method": "setMargin", "params": args})

    def setwidth(self, width):
        """Sets the width of this View. Can be either an integer describing the value in dp, "MATCH_PARENT" or "WRAP_CONTENT"."""
        self.a.c.send_msg({"method": "setWidth", "params": {"aid": self.a.aid, "id": self.id, "width": width}})

    def setheight(self, height):
        """Sets the height of this View. Can be either an integer describing the value in dp, "MATCH_PARENT" or "WRAP_CONTENT"."""
        self.a.c.send_msg({"method": "setHeight", "params": {"aid": self.a.aid, "id": self.id, "height": height}})

    def setdimensions(self, width, height):
        """Sets the dimensions of this view. width and height are the same as for setwidth and setheight."""
        self.a.setwidth(width)
        self.a.setheight(height)

    def setlinearlayoutparams(self, weight):
        """Sets the LinearLayout weight for this view."""
        self.a.c.send_msg({"method": "setLinearLayoutParams", "params": {"aid": self.a.aid, "id": self.id, "weight": weight}})
    
    
    def sendtouchevent(self, send):
        """Sets whether ot not touch events are send for this View."""
        self.a.c.send_msg({"method": "sendTouchEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    
    
    def handleevent(self, e):
        """Handles an Event for this View. Subclasses can override this to provide event handling."""
        pass






