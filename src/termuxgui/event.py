
class Event:
    
    # Event types
    # View events
    click = "click"
    longClick = "longClick"
    focusChange = "focusChange"
    key = "key"
    touch = "touch"
    refresh = "refresh"
    
    # activity events
    create = "create"
    start = "start"
    resume = "resume"
    pause = "pause"
    stop = "stop"
    destroy = "destroy"
    userleavehint = "UserLeaveHint"
    pipchanged = "pipchanged"
    
    # special overlay events
    overlaytouch = "overlayTouch"
    overlayScale = "overlayScale"
    
    
    def __init__(self, ev):
        self.type = ev["type"]
        try:
            self.value = ev["value"]
            if type(self.value) is dict:
                self.aid = self.value["aid"]
                self.id = self.value["id"]
        except KeyError:
            pass
        
    
