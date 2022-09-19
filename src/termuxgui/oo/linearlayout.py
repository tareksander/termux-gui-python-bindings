from typing import Optional, Literal

import termuxgui as tg

from termuxgui.activity import Activity
from termuxgui.oo.viewgroup import ViewGroup


class LinearLayout(ViewGroup, tg.LinearLayout):
    """This represents a LinearLayout."""

    def __init__(self, activity: Activity, parent: Optional[ViewGroup] = None, vertical: bool = True,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.LinearLayout.__init__(self, activity, parent, vertical, visibility)
        ViewGroup.__init__(self, activity, self.id, parent)
