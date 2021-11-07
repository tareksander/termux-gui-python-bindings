from json import dumps

from termuxgui.__send_read_msg import __send_read_msg

def activity(mainSocket, tid=None,flags=0,dialog=None,pip=False):
    '''Creates and Activity and returns the Activity and Task id.'''
    params = {"flags": flags}
    if dialog != None:
        params["dialog"] = dialog
    if tid != None:
        params["tid"] = tid
    if pip != None:
        params["pip"] = pip
    return __send_read_msg(mainSocket, dumps({"method": "newActivity", "params": params}))
