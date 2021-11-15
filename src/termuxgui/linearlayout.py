from json import dumps


from termuxgui.viewgroup import ViewGroup

class LinearLayout(ViewGroup):
    
    def __init__(self, activity, parent=None, vertical=True):
        args = {"aid": activity.aid, "vertical": vertical}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createLinearLayout", "params": args}))
    
    
    
    
    
    
    
    
    
    
    
