from json import dumps

from termuxgui.view import View

class TextView(View):
    """This represents a TextView."""
    
    def __init__(self, activity, text, parent=None, selectabletext=False, clickablelinks=False):
        args = {"aid": activity.aid, "text": text, "selectableText": selectabletext, "clickableLinks": clickablelinks}
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
    
    
    def settextcolor(self, color):
        """Sets the text color of this TextView. The color format is the same as for Activity.settheme()."""
        self.a.c.send_msg({"method": "setTextColor", "params": {"aid": self.a.aid, "id": self.id, "color": color}})
    
    
    def sendtextevent(self, send):
        """Sets whether ot not text events are send for this TextView."""
        self.a.c.send_msg({"method": "sendTextEvent", "params": {"aid": self.a.aid, "id": self.id, "send": send}})
    
    
