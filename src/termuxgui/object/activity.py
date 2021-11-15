from json import dumps

from termuxgui.__send_read_msg import __send_read_msg 
from termuxgui.__send_msg import __send_msg


from termuxgui.object.task import Task


class Activity:
    def __init__(self, connection, tid=None,dialog=None,pip=False,overlay=None,lockscreen=None):
        self.c = connection
        params = {}
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
            self.aid, tid = __send_read_msg(self.c._main, dumps({"method": "newActivity", "params": params}))
        else:
            self.aid = __send_read_msg(self.c._main, dumps({"method": "newActivity", "params": params}))
        self.t = Task(connection, tid)
        if self.aid == -1:
            raise RuntimeError("Could not create Activity")
    
    
    def finish(self):
    '''Finishes an Activity.'''
    __send_msg(self.c._main, dumps({"method": "finishActivity", "params": {"aid": self.aid}}))
    
    
    def setinputmode(mode):
    '''Sets the input mode for an Activity.'''
    __send_msg(self.c._main, dumps({"method": "setInputMode", "params": {"aid": self.aid, "mode": mode}}))
    
    def keepscreenon(on):
        __send_msg(self.c._main, dumps({"method": "keepScreenOn", "params": {"aid": self.aid, "on": on}}))
    
    def setpipmode(self, pip):
        __send_msg(self.c._main, dumps({"method": "setPiPMode", "params": {"aid": self.aid, "pip": pip}}))
    
    def setpipmodeauto(self, pip):
        __send_msg(self.c._main, dumps({"method": "setPiPModeAuto", "params": {"aid": self.aid, "pip": pip}}))
    
    def setpipparams(self, num, den):
    '''Sets the PiP parameters for the Activity, the aspect ration.'''
    __send_msg(self.c._main, dumps({"method": "setPiPParams", "params": {"aid": self.aid, "num": num, "den": den}}))
    
    def settaskdescription(self, text, img):
        '''Sets the Task icon. img has to be a PNG or JPEG image as a base64 encoded string.'''
        __send_msg(self.c._main, dumps({"method": "setTaskDescription", "params": {"aid": self.aid, "img": img, "label": text}}))
    
    def settheme(self, statusbarcolor, colorprimary, windowbackground, textcolor, coloraccent):
    '''Sets the Theme fro an Activity.'''
    __send_msg(self.c._main, dumps({"method": "setTheme", "params": {"aid": self.aid, "statusBarColor": statusbarcolor, "colorPrimary": colorprimary, "windowBackground": windowbackground, "textColor": textcolor, "colorAccent": coloraccent}}))
    
    def setorientation(orientation):
        __send_msg(self.c._main, dumps({"method": "setOrientation", "params": {"aid": self.aid, "orientation": orientation}}))
    
    
    

    def setposition(x, y):
        __send_msg(self.c._main, dumps({"method": "setPosition", "params": {"aid": self.aid, "x": x, "y": y}}))



    def sendoverlayevents(send):
        __send_msg(self.c._main, dumps({"method": "sendOverlayTouchEvent", "params": {"aid": self.aid, "send": send}}))
    
    
    
    

