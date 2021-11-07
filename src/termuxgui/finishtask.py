from json import dumps

from termuxgui.__send_msg import __send_msg

def finishtask(mainSocket, tid):
    '''Finishes a Task and removes it from the recent tasks screen.'''
    __send_msg(mainSocket, dumps({"method": "finishTask", "params": {"tid": tid}}))
