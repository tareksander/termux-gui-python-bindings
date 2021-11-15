from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.view import View

class ImageView(View):
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, __send_read_msg(activity.c._main, dumps({"method": "createImageView", "params": args})))
    
    
    
    def setimage(self, img):
        __send_msg(self.a.c._main, dumps({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id, "img": base64.standard_b64encode(img).decode("ascii")}}))
    
    def setbuffer(self, b):
        __send_msg(self.a.c._main, dumps({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id, "bid": b.bid}}))
    
    def refresh(self):
        __send_msg(self.a.c._main, dumps({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id}}))
    
