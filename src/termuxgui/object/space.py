from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg
from termuxgui.object.view import View

class Space(View):
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        View.__init__(self, activity, __send_read_msg(mainSocket, dumps({"method": "createSpace", "params": args})))
    
