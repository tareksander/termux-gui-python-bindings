from json import dumps

from termuxgui.__send_read_msg import __send_read_msg 
from termuxgui.__send_msg import __send_msg

class Task:
    def __init__(self, connection, tid):
        self.c = connection
        self.tid = tid
    
    def finish(self):
        __send_msg(self.c._main, dumps({"method": "finishTask", "params": {"tid": self.tid}}))
    
    def bringtofront(self):
        __send_msg(self.c._main, dumps({"method": "bringTaskToFront", "params": {"tid": self.tid}}))
    
    def movetoback(self):
        __send_msg(self.c._main, dumps({"method": "moveTaskToBack", "params": {"tid": self.tid}}))
 
