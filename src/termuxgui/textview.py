from json import dumps

from termuxgui.view import View

class TextView(View):
    """This represents a TextView."""
    
    def __init__(self, activity, text, parent=None):
        args = {"aid": activity.aid, "text": text}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createTextView", "params": args}))
    
    def settextsize(self, size):
        """Sets the text size for this TextView."""
        self.a.c.send_msg({"method": "setTextSize", "params": {"aid": self.a.aid, "id": self.id, "size": size}})
    
    
    def gettext(self):
        """Gets the text of this TextView."""
        return self.a.c.send_read_msg({"method": "getText", "params": {"aid": self.a.aid, "id": self.id}})
    
    def settext(self, text):
        """Sets the text of this TextView."""
        self.a.c.send_msg({"method": "setText", "params": {"aid": self.a.aid, "id": self.id, "text": text}})
    
    
    
    
