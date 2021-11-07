from termuxgui.__read_msg import __read_msg
from termuxgui.__send_msg import __send_msg

def __send_read_msg(s, msg):
    __send_msg(s, msg)
    return __read_msg(s)
