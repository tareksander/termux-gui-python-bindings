from json import dumps

from termuxgui.__send_read_msg import __send_read_msg

def activity(mainSocket, tid=None,dialog=None,pip=False,overlay=None,lockscreen=None):
    '''Creates and Activity and returns the Activity and Task id.'''
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
    return __send_read_msg(mainSocket, dumps({"method": "newActivity", "params": params}))



def keepscreenon(mainSocket, aid, on):
    __send_msg(mainSocket, dumps({"method": "keepScreenOn", "params": {"aid": aid, "on": on}}))



def setorientation(mainSocket, aid, orientation):
    __send_msg(mainSocket, dumps({"method": "setOrientation", "params": {"aid": aid, "orientation": orientation}}))


def setposition(mainSocket, aid, x, y):
    __send_msg(mainSocket, dumps({"method": "setPosition", "params": {"aid": aid, "x": x, "y": y}}))


def setposition(mainSocket, aid, x, y):
    __send_msg(mainSocket, dumps({"method": "setPosition", "params": {"aid": aid, "x": x, "y": y}}))

def sendoverlayevents(mainSocket, aid, send):
    __send_msg(mainSocket, dumps({"method": "sendOverlayTouchEvent", "params": {"aid": aid, "send": send}}))

