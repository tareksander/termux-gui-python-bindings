
class Event:
    """This represents an Event in the GUI.
    
    The class variables are the available event types.
    
    Use ev.type == Event.eventtype to check for event types.
    
    ev.type contains the event type and ev.value is a dictionary containing the values of the event, if any."""
    
    
    # Event types
    # View events
    click = "click"
    longClick = "longClick"
    focusChange = "focusChange"
    key = "key"
    touch = "touch"
    refresh = "refresh"
    selected = "selected" # used for RadioGroups
    itemselected = "itemselected"
    
    
    
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
        self.value = {}
        try:
            self.value = ev["value"]
            if type(self.value) is dict:
                self.aid = self.value["aid"]
                self.id = self.value["id"]
        except KeyError:
            pass
        
    
