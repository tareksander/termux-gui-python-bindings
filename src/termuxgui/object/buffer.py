from json import dumps
from mmap import mmap
import os

from termuxgui.__send_read_msg  import __send_read_msg
from termuxgui.__send_msg import __send_msg


class Buffer:
    
    def __init__(self, connection, w, h, format="ARGB888"):
        self.c = connection
        ret = __send_read_msg(self.c._main, dumps({"method": "addBuffer", "params": {"w": w, "h": h, "format": format}}))
        if len(ret) == -1:
            raise RuntimeError("Could not create Buffer")
        self.bid, self.fd = ret
        self.mem = mmap(self.fd, w*h*4)
    
    def __enter__(self):
        return self.mem
    
    def __exit__(self, type, value, traceback):
        self.remove()
        return False
    
    
    def remove(self):
        __send_msg(self.c._main, dumps({"method": "deleteBuffer", "params": {"bid": self.bid}}))
        self.mem.close()
        os.close(self.fd)
    
    def blit(self):
        self.mem.flush()
        __send_msg(self.c._main, dumps({"method": "blitBuffer", "params": {"bid": self.bid}}))
    
    
    
    
    
