from termuxgui.compoundbutton import CompoundButton


class Switch(CompoundButton):
    """This represents a Switch."""

    def __init__(self, activity, text, parent=None, checked=False):
        args = {"aid": activity.aid, "text": text, "checked": checked}
        if parent is not None:
            args["parent"] = parent.id
        self.checked = checked
        CompoundButton.__init__(self, activity, activity.c.send_read_msg({"method": "createSwitch", "params": args}))
