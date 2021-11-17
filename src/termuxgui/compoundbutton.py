from json import dumps

from termuxgui.button import Button

class CompoundButton(Button):

    def handleevent(self, e):
        """Use this to let the CompoundButton track whether it is checked or not. Just pass every Event here."""
        if e.type == "click" and e.aid == self.a.aid and e.id == self.id:
            self.checked = e.value["set"]
    
    
    
    
    
    def setchecked(self, checked):
        self.checked = checked
        self.a.c.send_msg({"method": "setChecked", "params": {"aid": self.a.aid, "id": self.id, "checked": checked}})
    
