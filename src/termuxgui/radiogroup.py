from typing import Optional, Literal

from termuxgui.view import View
from termuxgui.activity import Activity
from termuxgui.linearlayout import LinearLayout
from termuxgui.viewgroup import ViewGroup


class RadioGroup(LinearLayout):
    """This represents a RadioGroup.

    Only one RadioButton inside a RadioGroup can be checked at once, and the RadioGroup emits events when the checked button has changed."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createRadioGroup", "params": args}))
