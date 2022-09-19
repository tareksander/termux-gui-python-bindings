from typing import Optional, Literal

import termuxgui as tg

from termuxgui.activity import Activity
from termuxgui.oo.framelayout import FrameLayout
from termuxgui.oo.viewgroup import ViewGroup


class HorizontalScrollView(FrameLayout, tg.HorizontalScrollView):
    """This represents a HorizontalScrollView."""

    def __init__(self, activity: Activity, parent: Optional[ViewGroup] = None, fillviewport: bool = False,
                 snapping: bool = False, nobar: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.HorizontalScrollView.__init__(self, activity, parent, fillviewport, snapping, nobar, visibility)
        ViewGroup.__init__(self, activity, self.id, parent)
