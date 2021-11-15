from json import dumps

from termuxgui.textview import TextView
from termuxgui.view import View

class Button(TextView):
    
    def __init__(self, activity, text, parent=None):
        args = {"aid": activity.aid, "text": text}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createButton", "params": args}))
     
     
     
     
     
     
