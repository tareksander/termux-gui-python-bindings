from abc import ABC
from typing import Optional, TYPE_CHECKING

import termuxgui as tg
from termuxgui.activity import Activity


class View(tg.View, ABC):
    """This represents a generic View."""
    
    def __init__(self, activity: Activity, id: int, parent: Optional['termuxgui.oo.viewgroup.ViewGroup']):
        tg.View.__init__(self, activity, id)
        self.parent = parent
        if self.parent:
            parent.views.append(self)
        else:
            activity.root = self
    
    def delete(self):
        """Deletes this View from the layout."""
        if self.parent:
            self.parent.views.remove(self)
        tg.View.delete(self)


if TYPE_CHECKING:
    import termuxgui.oo.viewgroup
