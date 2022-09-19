from typing import Optional, Literal

import termuxgui as tg

from termuxgui.activity import Activity
from termuxgui.oo.viewgroup import ViewGroup


class GridLayout(ViewGroup, tg.GridLayout):
    """This represents a GridLayout."""

    def __init__(self, activity: Activity, rows: int, cols: int, parent: Optional[ViewGroup] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.GridLayout.__init__(self, activity, rows, cols, parent, visibility)
        ViewGroup.__init__(self, activity, self.id, parent)
