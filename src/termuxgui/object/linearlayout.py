from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.viewgroup import ViewGroup

class LinearLayout(ViewGroup):
    
    def __init__(self, activity, parent=None, vertical=True):
        args = {"aid": activity.aid, "vertical": vertical}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createLinearLayout", "params": args})))
    
    
    
    
    
    
    
    
    
    
    
