from termuxgui.view import View


class ProgressBar(View):
    """This represents a ProgressBar."""

    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createProgressBar", "params": args}))

    def setprogress(self, progress):
        """Sets the progress of the ProgressBar. The progress has to be an integer from 0 to 100 (inclusive)."""
        self.a.c.send_msg({"method": "setProgress", "params": {"aid": self.a.aid, "id": self.id, "progress": progress}})
