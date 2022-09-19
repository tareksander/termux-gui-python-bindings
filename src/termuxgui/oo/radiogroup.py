from typing import Optional, Literal

import termuxgui as tg
from termuxgui.oo.view import View
from termuxgui.oo.viewgroup import ViewGroup


class RadioGroup(ViewGroup, tg.RadioGroup):
    """This represents a RadioGroup.

    Only one RadioButton inside a RadioGroup can be checked at once, and the RadioGroup emits events when the checked button has changed."""

    def __init__(self, activity: tg.Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.RadioGroup.__init__(self, activity, parent, visibility)
        ViewGroup.__init__(self, activity, self.id, parent)
