from json import dumps

from termuxgui.horizontalscrollview import HorizontalScrollView
from termuxgui.viewgroup import ViewGroup

class TabLayout(HorizontalScrollView):
    """This represents a TabLayout."""
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createTabLayout", "params": args}))
    
    
    
    def setlist(self, list):
        """Sets the list tabs. list has to be a list containing strings."""
        self.a.c.send_msg({"method": "setList", "params": {"aid": self.a.aid, "id": self.id, "list": list}})
    
    
    
