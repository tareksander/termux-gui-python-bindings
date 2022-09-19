from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class RadioButton(View, tg.RadioButton):
    """This represents a RadioButton."""

    def __init__(self, activity: tg.Activity, text: str, parent: Optional[View] = None, checked: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.RadioButton.__init__(self, activity, text, parent, checked, visibility)
        View.__init__(self, activity, self.id, parent)
