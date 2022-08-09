from typing import Optional, Literal

from termuxgui.activity import Activity
from termuxgui.view import View


class TextView(View):
    """This represents a TextView."""

    def __init__(self, activity: Activity, text: str, parent: Optional[View] = None, selectabletext: bool = False,
                 clickablelinks: bool = False, visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "text": text, "selectableText": selectabletext, "clickableLinks": clickablelinks,
                "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createTextView", "params": args}))

    def settextsize(self, size: int):
        """Sets the text size for this TextView."""
        self.a.c.send_msg({"method": "setTextSize", "params": {"aid": self.a.aid, "id": self.id, "size": size}})

    def gettext(self) -> str:
        """Gets the text of this TextView."""
        return self.a.c.send_read_msg({"method": "getText", "params": {"aid": self.a.aid, "id": self.id}})

    def settext(self, text: str):
        """Sets the text of this TextView."""
        self.a.c.send_msg({"method": "setText", "params": {"aid": self.a.aid, "id": self.id, "text": text}})

    def settextcolor(self, color: int):
        """Sets the text color of this TextView. The color format is the same as for Activity.settheme()."""
        self.a.c.send_msg({"method": "setTextColor", "params": {"aid": self.a.aid, "id": self.id, "color": color}})

    def sendtextevent(self, send: bool):
        """Sets whether ot not text events are send for this TextView."""
        self.a.c.send_msg({"method": "sendTextEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    def setgravity(self, horizontal: Literal[0, 1, 2], vertical: Literal[0, 1, 2]):
        """Sets the text gravity for this TextView.
        The values are: 0: left/top, 1: center, 2: right/bottom.
        Right and left are inverted for right-to-left layouts."""
        self.a.c.send_msg({"method": "setGravity", "params": {"aid": self.a.aid, "id": self.id,
                                                              "horizontal": horizontal, "vertical": vertical}})
