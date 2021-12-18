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

    def setwidth(self, width, px=False):
        """Sets the width of this View. Can be either an integer describing the value in dp, "MATCH_PARENT" or "WRAP_CONTENT". If px is true, the values are in pixels instead."""
        self.a.c.send_msg({"method": "setWidth", "params": {"aid": self.a.aid, "id": self.id, "width": width, "px": px}})

    def setheight(self, height, px=False):
        """Sets the height of this View. Can be either an integer describing the value in dp, "MATCH_PARENT" or "WRAP_CONTENT". If px is true, the values are in pixels instead."""
        self.a.c.send_msg({"method": "setHeight", "params": {"aid": self.a.aid, "id": self.id, "height": height, "px": px}})

    def setdimensions(self, width, height, px=False):
        """Sets the dimensions of this view. width and height are the same as for setwidth and setheight. If px is true, the values are in pixels instead."""
        self.setwidth(width, px)
        self.setheight(height, px)

    def setlinearlayoutparams(self, weight):
        """Sets the LinearLayout weight for this view."""
        self.a.c.send_msg({"method": "setLinearLayoutParams", "params": {"aid": self.a.aid, "id": self.id, "weight": weight}})
    
    
    def sendtouchevent(self, send):
        """Sets whether ot not touch events are send for this View."""
        self.a.c.send_msg({"method": "sendTouchEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    def sendclickevent(self, send):
        """Sets whether ot not click events are send for this View."""
        self.a.c.send_msg({"method": "sendClickEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    
    def sendlongclickevent(self, send):
        """Sets whether ot not long click events are send for this View."""
        self.a.c.send_msg({"method": "sendLongClickEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    def sendfocuschangeevent(self, send):
        """Sets whether ot not focus change events are send for this View."""
        self.a.c.send_msg({"method": "sendFocusChangeEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    
    def getdimensions(self):
        """Gets the width and height of a View in the layout as a list. The values are in pixels."""
        return self.a.c.send_read_msg({"method": "getDimensions", "params": {"aid": self.a.aid, "id": self.id}})
    
    
    def setbackgroundcolor(self, color):
        """Sets the background color for this view."""
        self.a.c.send_msg({"method": "setBackgroundColor", "params": {"aid": self.a.aid, "id": self.id, "color": color}})
    
    def setvisibility(self, vis):
        """Sets the visibilityr for this view.
        
        0 = gone, 1 = hidden, 2 = visible. While hidden, views are not visible but still take up space in the layout. Gone views do not take up layout space."""
        self.a.c.send_msg({"method": "setVisibility", "params": {"aid": self.a.aid, "id": self.id, "vis": vis}})
    
    
    def focus(self, forcesoft=False):
        """Sets the Focus to this View and opens the soft keyboard if the View has keyboard input."""
        self.a.c.send_msg({"method": "requestFocus", "params": {"aid": self.a.aid, "id": self.id, "forcesoft": forcesoft}})
    
    
    def handleevent(self, e):
        """Handles an Event for this View. Subclasses can override this to provide event handling."""
        pass






