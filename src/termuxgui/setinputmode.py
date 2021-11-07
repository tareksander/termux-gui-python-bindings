from json import dumps

from termuxgui.__send_msg import __send_msg

def setinputmode(mainSocket, aid, mode):
    '''Sets the input mode for an Activity.'''
    __send_msg(mainSocket, dumps({"method": "setInputMode", "params": {"aid": aid, "mode": mode}}))
 
