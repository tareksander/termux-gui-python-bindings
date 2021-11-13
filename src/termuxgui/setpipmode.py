from json import dumps

from termuxgui.__send_msg import __send_msg

def setpipmode(mainSocket, aid, pip):
    __send_msg(mainSocket, dumps({"method": "setPiPMode", "params": {"aid": aid, "pip": pip}}))
 
def setpipmodeauto(mainSocket, aid, pip):
    __send_msg(mainSocket, dumps({"method": "setPiPModeAuto", "params": {"aid": aid, "pip": pip}}))
