from json import dumps

from termuxgui.__send_msg import __send_msg

def bringtasktofront(mainSocket, tid):
    '''Bring an existing Task to the front and shows it.'''
    __send_msg(mainSocket, dumps({"method": "bringTaskToFront", "params": {"tid": tid}}))
