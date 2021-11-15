from mmap import mmap
import os

import termuxgui.msg as msg

class Buffer:
    
    def __init__(self, connection, w, h, format="ARGB888"):
        self.c = connection
        c.send_msg({"method": "addBuffer", "params": {"w": w, "h": h, "format": format}})
        ret = msg.read_msg_fd(self.c._main,)
        if len(ret) == 1:
            raise RuntimeError("Could not create Buffer")
        self.bid, self.fd = ret
        self.mem = mmap(self.fd, w*h*4)
    
    def __enter__(self):
        return self.mem
    
    def __exit__(self, type, value, traceback):
        self.remove()
        return False
    
    
    def remove(self):
        self.c.send_msg({"method": "deleteBuffer", "params": {"bid": self.bid}})
        self.mem.close()
        os.close(self.fd)
    
    def blit(self):
        self.mem.flush()
        self.c.send_msg({"method": "blitBuffer", "params": {"bid": self.bid}})
    
    
    
    
    
