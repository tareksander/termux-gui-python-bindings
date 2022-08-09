from termuxgui.activity import Activity
from termuxgui.button import Button
from termuxgui.event import Event
from termuxgui.view import View


class CompoundButton(Button):
    """This represents a CompoundButton.

    This class doesn't correspond to a particular View, it is used to provide common methods for all CompoundButtons."""

    def __init__(self, activity: Activity, id: int):
        View.__init__(self, activity, id)
        self.checked = False

    def handleevent(self, e: Event):
        """Use this to let the CompoundButton track whether it is checked or not. Just pass every Event here."""
        if e.type == Event.click and e.aid == self.a.aid and e.id == self.id:
            self.checked = e.value["set"]
        View.handleevent(self, e)

    def setchecked(self, checked: bool):
        """Explicitly set the checked status of this CompoundButton."""
        self.checked = checked
        self.a.c.send_msg({"method": "setChecked", "params": {"aid": self.a.aid, "id": self.id, "checked": checked}})
