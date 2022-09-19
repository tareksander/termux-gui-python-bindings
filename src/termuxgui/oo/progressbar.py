from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class ProgressBar(View, tg.ProgressBar):
    """This represents a ProgressBar."""

    def __init__(self, activity: tg.Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.ProgressBar.__init__(self, activity, parent, visibility)
        View.__init__(self, activity, self.id, parent)

