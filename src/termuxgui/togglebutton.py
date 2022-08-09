from typing import Optional, Literal

from termuxgui.view import View
from termuxgui.activity import Activity
from termuxgui.compoundbutton import CompoundButton


class ToggleButton(CompoundButton):
    """This represents a ToggleButton."""

    def __init__(self, activity: Activity, parent: Optional[View] = None, checked: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "checked": checked, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        self.checked = checked
        CompoundButton.__init__(self, activity, activity.c.send_read_msg({"method": "createToggleButton", "params": args}))
