from mmap import mmap
import os
from typing import Literal

import termuxgui.msg as msg


class Buffer:
    """This represents a raw ARGB888 image buffer.

    This is only available on Android 8.1+.
    Buffers consume much memory, so be sure to close any Buffer you don't need any more.
    Preferably use "with" to get the memory object of the buffer so it is automatically closed.
    The memory object is a shared memory object that can be used like a bytes object or a file object.
    You can also directly access the memory object as b.mem.

    A RuntimeError is raised when a Buffer can't be created."""

    def __init__(self, connection, w: int, h: int, format: Literal["ARGB888"] = "ARGB888"):
        self.c = connection
        self.c.send_msg({"method": "addBuffer", "params": {"w": w, "h": h, "format": format}})
        ret = msg.read_msg_fd(self.c._main)
        if len(ret) == 1:
            raise RuntimeError("Could not create Buffer")
        self.bid, self.fd = ret
        self.mem = mmap(self.fd, w * h * 4)

    def __enter__(self):
        return self.mem

    def __exit__(self, type, value, traceback):
        self.remove()
        return False

    def remove(self):
        """Removes this buffer, freeing the memory."""
        self.c.send_msg({"method": "deleteBuffer", "params": {"bid": self.bid}})
        self.mem.close()
        os.close(self.fd)

    def blit(self):
        """Blits the buffer to the underlying image in the plugin.
        To update ImageViews using this buffer, they have to be refreshed afterwards."""
        self.mem.flush()
        self.c.send_msg({"method": "blitBuffer", "params": {"bid": self.bid}})
