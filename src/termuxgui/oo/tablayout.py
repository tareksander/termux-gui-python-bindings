from typing import Optional, Literal

import termuxgui as tg
from termuxgui.oo.viewgroup import ViewGroup


class TabLayout(ViewGroup, tg.TabLayout):
    """This represents a TabLayout."""

    def __init__(self, activity: tg.Activity, parent: Optional[ViewGroup] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.TabLayout.__init__(self, activity, parent, visibility)
        ViewGroup.__init__(self, activity, self.id, parent)


    
