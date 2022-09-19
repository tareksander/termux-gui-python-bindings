from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View
from termuxgui.activity import Activity
from termuxgui.oo.viewgroup import ViewGroup


class SwipeRefreshLayout(ViewGroup, tg.SwipeRefreshLayout):
    """This represents a SwipeRefreshLayout."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.SwipeRefreshLayout.__init__(self, activity, parent, visibility)
        ViewGroup.__init__(self, activity, self.id, parent)

