from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class Space(View, tg.Space):
    """This represents a Space. You can use this to create empty space in your layout."""

    def __init__(self, activity: tg.Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.Space.__init__(self, activity, parent, visibility)
        View.__init__(self, activity, self.id, parent)
