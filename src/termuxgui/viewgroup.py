from json import dumps

from termuxgui.view import View

class ViewGroup(View):
    
    def __init__(self, activity, id):
        View.__init__(self, activity, id)
    
    
    def clearchildren(self):
        self.a.c.send_msg({"method": "deleteChildren", "params": {"aid": self.a.aid, "id": self.id}})
    
    
    
    
 
