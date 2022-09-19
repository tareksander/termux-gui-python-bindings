from typing import Optional, Literal

import termuxgui as tg

from termuxgui.oo.view import View


class EditText(View, tg.EditText):
    """This represents an EditText."""

    def __init__(self, activity: tg.Activity, text: str, parent: Optional[View] = None, singleline: bool = False,
                 line: bool = True, blockinput: bool = False,
                 inputtype: Literal["text", "textMultiLine", "phone", "date", "time", "datetime", "number",
                                    "numberDecimal", "numberPassword", "numberSigned", "numberDecimalSigned",
                                    "textEmailAddress", "textPassword"] = "text",
                 visibility: Optional[Literal[0, 1, 2]] = None):
        tg.EditText.__init__(self, activity, text, parent, singleline, line, blockinput, inputtype, visibility)
        View.__init__(self, activity, self.id, parent)

