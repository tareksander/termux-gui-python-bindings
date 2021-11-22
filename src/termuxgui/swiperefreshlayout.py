from json import dumps

from termuxgui.viewgroup import ViewGroup

class SwipeRefreshLayout(ViewGroup):
    """This represents a SwipeRefreshLayout."""
    
    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent != None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createSwipeRefreshLayout", "params": args}))
    
    def setrefreshing(self, refreshing):
        """Sets whether the SwipeRefreshLayout displays the refresh animation.
        
        You have to call this with False when you refreshed the contents."""
        self.a.c.send_msg({"method": "setRefreshing", "params": {"aid": self.a.aid, "id": self.id, "refresh": refreshing}})
    
    
    
