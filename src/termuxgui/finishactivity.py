from json import dumps

from termuxgui.__send_msg import __send_msg

def finishactivity(mainSocket, aid):
    '''Finishes an Activity. For the first Activity in a Task, use finishTask instead.'''
    __send_msg(mainSocket, dumps({"method": "finishActivity", "params": {"aid": aid}}))
