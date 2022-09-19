from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class TextView(View, tg.TextView):
    """This represents a TextView."""

    def __init__(self, activity: tg.Activity, text: str, parent: Optional[View] = None, selectabletext: bool = False,
                 clickablelinks: bool = False, visibility: Optional[Literal[0, 1, 2]] = None):
        tg.TextView.__init__(self, activity, text, parent, selectabletext, clickablelinks, visibility)
        View.__init__(self, activity, self.id, parent)
    