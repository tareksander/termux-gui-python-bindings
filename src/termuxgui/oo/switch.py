from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class Switch(View, tg.Switch):
    """This represents a Switch."""

    def __init__(self, activity: tg.Activity, text: str, parent: Optional[View] = None, checked: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.Switch.__init__(self, activity, text, parent, checked, visibility)
        View.__init__(self, activity, self.id, parent)
