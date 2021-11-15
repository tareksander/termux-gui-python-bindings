from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.textview import TextView
from termuxgui.object.view import View

class Checkbox(TextView):
    
    def __init__(self, activity, text, parent=None, checked=False):
        args = {"aid": activity.aid, "text": text, "checked": checked}
        if parent != None:
            args["parent"] = parent.id
        self.checked = checked
        View.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createCheckbox", "params": args})))
     
     
     
     def handleevent(self, e):
        """Use this to let the CheckBox track whether it is checked or not. Just pass every Event here."""
        if e.type == "click" and e.aid == self.a.aid and e.id == self.id:
            self.checked = e.value["set"]
     
     
