from termuxgui.compoundbutton import CompoundButton


class ToggleButton(CompoundButton):
    """This represents a ToggleButton."""

    def __init__(self, activity, parent=None, checked=False):
        args = {"aid": activity.aid, "checked": checked}
        if parent is not None:
            args["parent"] = parent.id
        self.checked = checked
        CompoundButton.__init__(self, activity, activity.c.send_read_msg({"method": "createToggleButton", "params": args}))
