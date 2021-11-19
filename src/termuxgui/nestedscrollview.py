from json import dumps

from termuxgui.framelayout import FrameLayout
from termuxgui.viewgroup import ViewGroup

class NestedScrollView(FrameLayout):
    """This represents a NestedScrollView."""
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createNestedScrollView", "params": args}))
    
    
    
 
