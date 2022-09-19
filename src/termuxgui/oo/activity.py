from typing import Optional

import termuxgui as tg

from abc import ABC
from enum import Enum


class Activity(tg.Activity, ABC):
    """Abstract base class for Activities."""
    
    class Type(Enum):
        NORMAL = 1
        PIP = 2
        LOCKSCREEN = 3
        DIALOG = 4
        DIALOG_NO_CANCEL_OUTSIDE = 5

    def get_type(self) -> Type:
        """Return the type of your Activity here."""
        return Activity.Type.NORMAL

    def intercept_back(self) -> bool:
        """Specify if you want to intercept back events."""
        return False

    def __init__(self, c: tg.Connection, t: Optional[tg.Task]):
        args = {"intercept": self.intercept_back()}
        match self.get_type():
            case Activity.Type.PIP:
                args["pip"] = True
            case Activity.Type.DIALOG:
                args["dialog"] = True
            case Activity.Type.DIALOG_NO_CANCEL_OUTSIDE:
                args["dialog"] = True
                args["canceloutside"] = False
        if t is not None:
            args["tid"] = t.tid
        tg.Activity.__init__(self, c, **args)
        self.root = None
    
    def on_create(self):
        pass

    def on_start(self):
        pass

    def on_resume(self):
        pass

    def on_pause(self, finishing: bool):
        pass

    def on_stop(self, finishing: bool):
        pass

    def on_destroy(self, finishing: bool):
        pass

    def on_back(self):
        pass

    def on_userleavehint(self):
        pass

    def on_pipchanged(self, pip: bool):
        pass

    def on_config(self, config: tg.activity.Configuration):
        pass
