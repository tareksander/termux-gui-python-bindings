from termuxgui.__read_msg  import __read_msg 


def getevent(eventSocket):
    '''Blocks until a Event is available and returns it.'''
    return __read_msg(eventSocket)

