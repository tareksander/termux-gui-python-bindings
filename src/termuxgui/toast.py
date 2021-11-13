from json import dumps

from termuxgui.__send_msg import __send_msg

def toast(mainSocket, text, long=False):
    __send_msg(mainSocket, dumps({"method": "toast", "params": {"text": text, "long": long}})) 
