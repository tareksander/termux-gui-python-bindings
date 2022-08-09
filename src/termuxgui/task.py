from termuxgui.connection import Connection


class Task:
    """This represents an Android Task. It is automatically created with the Activity."""

    def __init__(self, connection: Connection, tid: int):
        self.c = connection
        self.tid = tid

    def finish(self):
        """Finishes this Task."""
        self.c.send_msg({"method": "finishTask", "params": {"tid": self.tid}})

    def bringtofront(self):
        """Bring this Task to the front and make it visible to the user.
        Might require "overlay over other apps" permission."""
        self.c.send_msg({"method": "bringTaskToFront", "params": {"tid": self.tid}})
