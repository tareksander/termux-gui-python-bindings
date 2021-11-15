from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.view import View

class TextView(View):
    
    def __init__(self, activity, text, parent=None):
        args = {"aid": activity.aid, "text": text}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createTextView", "params": args})))
    
    def settextsize(self, size):
        __send_msg(self.a.c._main, dumps({"method": "setTextSize", "params": {"aid": self.a.aid, "id": self.id, "size": size}}))
    
    
    def gettext(self):
        return __send_read_msg(self.a.c._main, dumps({"method": "getText", "params": {"aid": self.a.aid, "id": self.id}}))
    
    def settext(self, text):
        __send_msg(self.a.c._main, dumps({"method": "setText", "params": {"aid": self.a.aid, "id": self.id, "text": text}}))
    
    
    
    
