from typing import Optional, List, Literal

from termuxgui.activity import Activity
from termuxgui.view import View


class Spinner(View):
    """This represents a Spinner."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createSpinner", "params": args}))

    def setlist(self, list: List[str]):
        """Sets the list of items displayed in the Spinner."""
        self.a.c.send_msg({"method": "setList", "params": {"aid": self.a.aid, "id": self.id, "list": list}})

    def selectitem(self, item: int):
        """Sets the selected item of the Spinner."""
        self.a.c.send_msg({"method": "selectItem", "params": {"aid": self.a.aid, "id": self.id, "item": item}})
