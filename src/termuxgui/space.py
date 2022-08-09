from typing import Optional, Literal

from termuxgui.activity import Activity
from termuxgui.view import View


class Space(View):
    """This represents a Space. You can use this to create empty space in your layout."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createSpace", "params": args}))
