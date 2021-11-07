from json import dumps

from termuxgui.__send_msg import __send_msg

def settaskdescription(mainSocket, aid, text, img):
    '''Sets the Task icon. img has to be a PNG or JPEG image as a base64 encoded string.'''
    __send_msg(mainSocket, dumps({"method": "setTaskDescription", "params": {"aid": aid, "img": img, "label": text}}))
