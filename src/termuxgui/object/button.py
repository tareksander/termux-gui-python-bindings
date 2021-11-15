from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.textview import TextView
from termuxgui.object.view import View

class Button(TextView):
    
    def __init__(self, activity, text, parent=None):
        args = {"aid": activity.aid, "text": text}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createButton", "params": args})))
     
     
     
     
     
     
