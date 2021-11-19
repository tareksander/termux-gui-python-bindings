from json import dumps

from termuxgui.textview import TextView
from termuxgui.view import View

class EditText(TextView):
    """This represents an EditText."""
    
    def __init__(self, activity, text, parent=None, singleline=False, line=True, blockinput=False, inputtype="text"):
        args = {"aid": activity.aid, "text": text, "singleline": singleline, "line": line, "blockinput": blockinput, "type": inputtype}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createEditText", "params": args}))
    
    
    
    def showcursor(self, show):
        """Sets whether the cursor position should be shown."""
        self.a.c.send_msg({"method": "showCursor", "params": {"aid": self.a.aid, "id": self.id, "show": show}})
    
    
    
    
    
    
    
