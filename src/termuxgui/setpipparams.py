from json import dumps

from termuxgui.__send_msg import __send_msg

def setpipparams(mainSocket, aid, num, den):
    '''Sets the PiP parameters for the Activity, the aspect ration.'''
    __send_msg(mainSocket, dumps({"method": "setPiPParams", "params": {"aid": aid, "num": num, "den": den}}))
