from json import dumps

from termuxgui.viewgroup import ViewGroup

class FrameLayout(ViewGroup):
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createFrameLayout", "params": args}))
    
    
    
