from typing import Optional, Literal

from termuxgui.activity import Activity
from termuxgui.textview import TextView
from termuxgui.view import View


class EditText(TextView):
    """This represents an EditText."""

    def __init__(self, activity: Activity, text: str, parent: Optional[View] = None, singleline: bool = False,
                 line: bool = True, blockinput: bool = False,
                 inputtype: Literal["text", "textMultiLine", "phone", "date", "time", "datetime", "number",
                                    "numberDecimal", "numberPassword", "numberSigned", "numberDecimalSigned",
                                    "textEmailAddress", "textPassword"] = "text",
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "text": text, "singleline": singleline, "line": line, "blockinput": blockinput,
                "type": inputtype, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createEditText", "params": args}))

    def showcursor(self, show: bool):
        """Sets whether the cursor position should be shown."""
        self.a.c.send_msg({"method": "showCursor", "params": {"aid": self.a.aid, "id": self.id, "show": show}})
