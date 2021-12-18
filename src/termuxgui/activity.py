from json import dumps


from termuxgui.task import Task


class Activity:
    """This represents an Android Activity.
    
    Use a.c to access the Connection object of an Activity and a.t to access the Task object."""
    
    def __init__(self, connection, tid=None, dialog=None, pip=False, overlay=None, lockscreen=None, canceloutside=True):
        """When an Activity could not be created, a RuntimeError is raised."""
        self.c = connection
        params = {"canceloutside": canceloutside}
        if dialog != None:
            params["dialog"] = dialog
        if tid != None:
            params["tid"] = tid
        if pip != None:
            params["pip"] = pip
        if overlay != None:
            params["overlay"] = overlay
        if lockscreen != None:
            params["lockscreen"] = lockscreen
        if tid == None:
            self.aid, tid = self.c.send_read_msg({"method": "newActivity", "params": params})
        else:
            self.aid = self.c.send_read_msg({"method": "newActivity", "params": params})
        self.t = Task(connection, tid)
        if self.aid == -1:
            raise RuntimeError("Could not create Activity")
    
    
    def finish(self):
        '''Finishes an Activity.'''
        self.c.send_msg({"method": "finishActivity", "params": {"aid": self.aid}})
    
    
    def setinputmode(mode):
        '''Sets the input mode for an Activity.'''
        self.c.send_msg({"method": "setInputMode", "params": {"aid": self.aid, "mode": mode}})
    
    def keepscreenon(on):
        """Sets whether the Activity should keep the screen on while it is showing."""
        self.c.send_msg({"method": "keepScreenOn", "params": {"aid": self.aid, "on": on}})
    
    def setpipmode(self, pip):
        """Goes into / out of picture-in-picture mode.
        
        When you exit pip, you Activity is put in the recent tasks list and not shown to the user."""
        self.c.send_msg({"method": "setPiPMode", "params": {"aid": self.aid, "pip": pip}})
    
    def setpipmodeauto(self, pip):
        """Set whether the Activity should automatically enter picture-in-picture mode when the user leaves the Activity."""
        self.c.send_msg({"method": "setPiPModeAuto", "params": {"aid": self.aid, "pip": pip}})
    
    def setpipparams(self, num, den):
        '''Sets the PiP parameters for the Activity, currently only the aspect ration.'''
        self.c.send_msg({"method": "setPiPParams", "params": {"aid": self.aid, "num": num, "den": den}})
    
    def settaskdescription(self, label, img):
        '''Sets the Task icon. img has to be a PNG or JPEG image as a base64 encoded string.'''
        self.c.send_msg({"method": "setTaskDescription", "params": {"aid": self.aid, "img": img, "label": label}})
    
    def settheme(self, statusbarcolor, colorprimary, windowbackground, textcolor, coloraccent):
        '''Sets the Theme for the Activity.'''
        self.c.send_msg({"method": "setTheme", "params": {"aid": self.aid, "statusBarColor": statusbarcolor, "colorPrimary": colorprimary, "windowBackground": windowbackground, "textColor": textcolor, "colorAccent": coloraccent}})
    
    def setorientation(orientation):
        """Sets the preferred orientation of the Activity."""
        self.c.send_msg({"method": "setOrientation", "params": {"aid": self.aid, "orientation": orientation}})
    
    
    

    def setposition(x, y):
        """Sets the screen position of the Activity if it is an overlay."""
        self.c.send_msg({"method": "setPosition", "params": {"aid": self.aid, "x": x, "y": y}})



    def sendoverlayevents(send):
        """Sets whether or not you want to receive overlay events if the Activity is an overlay."""
        self.c.send_msg({"method": "sendOverlayTouchEvent", "params": {"aid": self.aid, "send": send}})
    
    
    def movetoback(self):
        """Moves this Activity's Task to the recents screen and hides it."""
        self.c.send_msg({"method": "moveTaskToBack", "params": {"aid": self.aid}})
    
    
    def requestunlock(self):
        """Requests the lockscreen to unlock. If the lockscreen is just protected by a swipe, it is unlocked immediately. If a PIN, password or pattern has to be used, brings up the UI to let the user unlock the lockscreen."""
        self.c.send_msg({"method": "requestUnlock", "params": {"aid": self.aid}})
    
    def getconfiguration(self):
        """Moves this Activity's Task to the recents screen and hides it."""
        return self.c.send_read_msg({"method": "getConfiguration", "params": {"aid": self.aid}})
    
    def hidesoftkeyboard(self):
        """Hides the soft keyboard if this Activity has the soft keyboard focus."""
        self.c.send_msg({"method": "hideSoftKeyboard", "params": {"aid": self.aid}})
    
    
    
    
