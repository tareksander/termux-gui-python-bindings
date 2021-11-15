from json import dumps


class Task:
    def __init__(self, connection, tid):
        self.c = connection
        self.tid = tid
    
    def finish(self):
        self.c.send_msg({"method": "finishTask", "params": {"tid": self.tid}})
    
    def bringtofront(self):
        self.c.send_msg({"method": "bringTaskToFront", "params": {"tid": self.tid}})
    
    def movetoback(self):
        self.c.send_msg({"method": "moveTaskToBack", "params": {"tid": self.tid}})
 
