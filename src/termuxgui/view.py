from typing import Optional, Literal, List, Union

from termuxgui.event import Event
from termuxgui.activity import Activity


class View:
    """This represents a generic View."""
    
    """Visibility constant for gone views"""
    GONE = 0
    
    """Visibility constant for hidden views"""
    HIDDEN = 1
    
    """Visibility constant for visible views"""
    VISIBLE = 2
    
    """Special size constant to only take up the space needed."""
    WRAP_CONTENT: str = "WRAP_CONTENT"

    """Special size constant to take up the space of the parent View."""
    MATCH_PARENT: str = "MATCH_PARENT"
    
    def __init__(self, activity: Activity, id: int):
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

    def setmargin(self, margin: int, dir: Optional[Literal["top", "bottom", "left", "right"]] = None):
        """Sets the margins of this View for one or all directions."""
        args = {"aid": self.a.aid, "id": self.id, "margin": margin}
        if dir is not None:
            args["dir"] = dir
        self.a.c.send_msg({"method": "setMargin", "params": args})

    def setwidth(self, width: Union[int, str], px: bool = False):
        """Sets the width of this View.
        Can be either an integer describing the value in dp, "MATCH_PARENT" or "WRAP_CONTENT".
        If px is true, the values are in pixels instead."""
        self.a.c.send_msg(
            {"method": "setWidth", "params": {"aid": self.a.aid, "id": self.id, "width": width, "px": px}})

    def setheight(self, height: Union[int, str], px: bool = False):
        """Sets the height of this View.
        Can be either an integer describing the value in dp, "MATCH_PARENT" or "WRAP_CONTENT".
        If px is true, the values are in pixels instead."""
        self.a.c.send_msg(
            {"method": "setHeight", "params": {"aid": self.a.aid, "id": self.id, "height": height, "px": px}})

    def setdimensions(self, width: Union[int, str],
                      height: Union[int, str], px: bool = False):
        """Sets the dimensions of this view. width and height are the same as for setwidth and setheight.
        If px is true, the values are in pixels instead."""
        self.setwidth(width, px)
        self.setheight(height, px)

    def setlinearlayoutparams(self, weight: int, position: Optional[int] = None):
        """Sets the LinearLayout weight and/or position for this view."""
        self.a.c.send_msg({"method": "setLinearLayoutParams",
                           "params": {"aid": self.a.aid, "id": self.id, "weight": weight, "position": position}})
    
    def setgridlayoutparams(self, row: int, col: int, rowsize: int = 1, colsize: int = 1,
                            alignmentrow: Literal["top", "bottom", "left", "right", "center", "baseline", "fill"] = "center",
                            alignmentcol: Literal["top", "bottom", "left", "right", "center", "baseline", "fill"] = "center"):
        """Sets the GridLayout position for this View.
        The rows and columns start at 0.
        rowsize and colsize define how many row/column cells a View takes up.
        alignmentrow and alignmentcol specify how the View is positioned in its cells,"""
        self.a.c.send_msg({"method": "setGridLayoutParams",
                           "params": {"aid": self.a.aid, "id": self.id, "row": row, "col": col,
                                      "colsize": colsize, "rowsize": rowsize,
                                      "alignmentrow": alignmentrow, "alignmentcol": alignmentcol}})
    
    def sendtouchevent(self, send: bool):
        """Sets whether ot not touch events are sent for this View."""
        self.a.c.send_msg({"method": "sendTouchEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})

    def sendclickevent(self, send: bool):
        """Sets whether ot not click events are sent for this View."""
        self.a.c.send_msg({"method": "sendClickEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})

    def sendlongclickevent(self, send: bool):
        """Sets whether ot not long click events are sent for this View."""
        self.a.c.send_msg({"method": "sendLongClickEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})

    def sendfocuschangeevent(self, send: bool):
        """Sets whether ot not focus change events are sent for this View."""
        self.a.c.send_msg(
            {"method": "sendFocusChangeEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})

    def getdimensions(self) -> List[int]:
        """Gets the width and height of a View in the layout as a list. The values are in pixels."""
        return self.a.c.send_read_msg({"method": "getDimensions", "params": {"aid": self.a.aid, "id": self.id}})

    def setbackgroundcolor(self, color: int):
        """Sets the background color for this view."""
        self.a.c.send_msg(
            {"method": "setBackgroundColor", "params": {"aid": self.a.aid, "id": self.id, "color": color}})

    def setvisibility(self, vis: Literal[0, 1, 2]):
        """Sets the visibility for this view.

        0 = gone, 1 = hidden, 2 = visible. While hidden, views are not visible but still take up space in the layout.
        Gone views do not take up layout space."""
        self.a.c.send_msg({"method": "setVisibility", "params": {"aid": self.a.aid, "id": self.id, "vis": vis}})

    def focus(self, forcesoft: bool = False):
        """Sets the Focus to this View and opens the soft keyboard if the View has keyboard input."""
        self.a.c.send_msg(
            {"method": "requestFocus", "params": {"aid": self.a.aid, "id": self.id, "forcesoft": forcesoft}})

    def handleevent(self, e: Event):
        """Handles an Event for this View. Subclasses can override this to provide event handling."""
        if hasattr(self, "eventlistener"):
            self.eventlistener(self, e)
    
    def setclickable(self, clickable: bool):
        """Sets whether the View is clickable by the user."""
        self.a.c.send_msg({"method": "setClickable", "params": {"aid": self.a.aid, "id": self.id, "clickable": clickable}})
    
