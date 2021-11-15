from json import dumps

from termuxgui.view import View

class Space(View):
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createSpace", "params": args}))
    
