from typing import Optional, Literal

from termuxgui.view import View
from termuxgui.activity import Activity
from termuxgui.viewgroup import ViewGroup


class SwipeRefreshLayout(ViewGroup):
    """This represents a SwipeRefreshLayout."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity,
                           activity.c.send_read_msg({"method": "createSwipeRefreshLayout", "params": args}))

    def setrefreshing(self, refreshing: bool):
        """Sets whether the SwipeRefreshLayout displays the refresh animation.

        You have to call this with False when you refreshed the contents."""
        self.a.c.send_msg(
            {"method": "setRefreshing", "params": {"aid": self.a.aid, "id": self.id, "refresh": refreshing}})
