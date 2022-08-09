from typing import Optional, List, Literal

from termuxgui.view import View
from termuxgui.activity import Activity
from termuxgui.framelayout import FrameLayout
from termuxgui.viewgroup import ViewGroup


class NestedScrollView(FrameLayout):
    """This represents a NestedScrollView."""

    def __init__(self, activity: Activity, parent: Optional[View] = None, fillviewport: bool = False,
                 snapping: bool = False, nobar: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "fillviewport": fillviewport, "snapping": snapping, "nobar": nobar,
                "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity,
                           activity.c.send_read_msg({"method": "createNestedScrollView", "params": args}))

    def getscrollposition(self) -> List[int]:
        """Gets the x and x scroll positions."""
        return self.a.c.send_read_msg({"method": "getScrollPosition", "params": {"aid": self.a.aid, "id": self.id}})

    def setscrollposition(self, x: int, y: int, smooth: bool = True):
        """Sets the x and x scroll positions. smooth specifies whether it's a smooth scroll or not."""
        self.a.c.send_msg({"method": "setScrollPosition",
                           "params": {"aid": self.a.aid, "id": self.id, "x": x, "y": y, "soft": smooth}})
