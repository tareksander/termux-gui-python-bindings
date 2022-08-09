from typing import Optional, Literal

from termuxgui.activity import Activity
from termuxgui.textview import TextView
from termuxgui.view import View


class Button(TextView):
    """This represents a Button."""

    def __init__(self, activity: Activity, text: str, parent: Optional[View] = None, allcaps: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "text": text, "allcaps": allcaps, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createButton", "params": args}))
