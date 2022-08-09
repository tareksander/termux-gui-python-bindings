from typing import Optional, Literal

from termuxgui.activity import Activity
from termuxgui.compoundbutton import CompoundButton
from termuxgui.view import View


class Checkbox(CompoundButton):
    """This represents a CheckBox."""

    def __init__(self, activity: Activity, text: str, parent: Optional[View] = None, checked: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "text": text, "checked": checked, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        self.checked = checked
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createCheckbox", "params": args}))
