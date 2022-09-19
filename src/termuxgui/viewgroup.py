from termuxgui.activity import Activity
from termuxgui.view import View


class ViewGroup(View):
    """This represents a generic ViewGroup."""

    def __init__(self, activity: Activity, id: int):
        View.__init__(self, activity, id)
    
    def clearchildren(self):
        """Removes all child Views of this ViewGroup."""
        self.a.c.send_msg({"method": "deleteChildren", "params": {"aid": self.a.aid, "id": self.id}})
