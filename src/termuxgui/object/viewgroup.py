from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.view import View

class ViewGroup(View):
    
    def __init__(self, activity, id):
        View.__init__(self, activity, id)
    
    
    def clearchildren(self):
        __send_msg(self.a.c._main, dumps({"method": "deleteChildren", "params": {"aid": self.a.aid, "id": self.id}}))
    
    
    
    
 
