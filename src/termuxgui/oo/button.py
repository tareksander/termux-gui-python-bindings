from typing import Optional, Literal

import termuxgui as tg

from termuxgui.activity import Activity
from termuxgui.oo.view import View


class Button(View, tg.Button):
    """This represents a Button."""

    def __init__(self, activity: Activity, text: str, parent: Optional[View] = None, allcaps: bool = False,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.Button.__init__(self, activity, text, parent, allcaps, visibility)
        View.__init__(self, activity, self.id, parent)
