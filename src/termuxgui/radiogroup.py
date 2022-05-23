from termuxgui.linearlayout import LinearLayout
from termuxgui.viewgroup import ViewGroup


class RadioGroup(LinearLayout):
    """This represents a RadioGroup.

    Only one RadioButton inside a RadioGroup can be checked at once, and the RadioGroup emits events when the checked button has changed."""

    def __init__(self, activity, parent=None):
        args = {"aid": activity.aid}
        if parent is not None:
            args["parent"] = parent.id
        ViewGroup.__init__(self, activity, activity.c.send_read_msg({"method": "createRadioGroup", "params": args}))
