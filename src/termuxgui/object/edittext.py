from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.textview import TextView
from termuxgui.object.view import View

class EditText(TextView):
    
    def __init__(self, activity, text, parent=None, singleline=False, line=True):
        args = {"aid": activity.aid, "text": text, "singleline": singleline, "line": line}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createEditText", "params": args})))
    
    
    
    def showcursor(self, show):
    __send_msg(self.a.c._main, dumps({"method": "showCursor", "params": {"aid": self.a.aid, "id": self.id, "show": show}}))
    
    
    
    
    
    
    
