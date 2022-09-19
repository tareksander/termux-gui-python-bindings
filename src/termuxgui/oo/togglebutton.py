from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class ToggleButton(View, tg.ToggleButton):
    """This represents a ToggleButton."""

    def __init__(self, activity: tg.Activity, parent: Optional[View] = None, checked: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.ToggleButton.__init__(self, activity, parent, checked, visibility)
        View.__init__(self, activity, self.id, parent)
