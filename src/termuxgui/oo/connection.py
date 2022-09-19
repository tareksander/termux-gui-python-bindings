from typing import Type, Optional

import termuxgui as tg
from termuxgui.oo.activity import Activity
from termuxgui.oo.view import View


def _dispatch_event_recursive(e: tg.Event, v: View) -> bool:
    if v.id == e.id:
        if hasattr(v, "on_"+e.type):
            getattr(v, "on_"+e.type)(e, v)
            return True
    if hasattr(v, "views"):
        views = getattr(v, "views")
        for child in views:
            ret = _dispatch_event_recursive(e, child)
            if ret:
                return True
    return False


class Connection(tg.Connection):
    """This represents a connection to the Termux:GUI plugin and contains all functions that don't act on any
    particular View, Activity or Task. """
    
    __activities: dict[str, Activity] = {}
    
    """Launches an Activity with the specified parameters."""
    def launch(self, activity: Type[Activity], t: Optional[tg.Task] = None, *args, **kwargs):
        a = activity(self, t, *args, *kwargs)
        self.__activities[a.aid] = a
    
    """Runs the event loop. Dispatches events to Activities and Views. Exits if there aren't any Activities anymore."""
    def event_loop(self):
        for e in self.events():
            if hasattr(e, "aid"):
                a = self.__activities[e.aid]
                if a is not None:
                    match [e.type]:
                        case [tg.Event.create]:
                            a.on_create()
                        case [tg.Event.start]:
                            a.on_start()
                        case [tg.Event.resume]:
                            a.on_resume()
                        case [tg.Event.pause]:
                            a.on_pause(e.value["finishing"])
                        case [tg.Event.stop]:
                            a.on_stop(e.value["finishing"])
                        case [tg.Event.destroy]:
                            a.on_destroy(e.value["finishing"])
                            del self.__activities[e.aid]
                        case [tg.Event.back]:
                            a.on_back()
                        case [tg.Event.userleavehint]:
                            a.on_userleavehint()
                        case [tg.Event.pipchanged]:
                            a.on_pipchanged(e.value)
                        case [tg.Event.config]:
                            a.on_config(e.value)
                        case [tg.Event.click | tg.Event.longClick | tg.Event.focusChange | tg.Event.key |
                              tg.Event.touch | tg.Event.refresh | tg.Event.selected | tg.Event.itemselected |
                              tg.Event.text | tg.Event.webviewNavigation | tg.Event.webviewHTTPError |
                              tg.Event.webviewError | tg.Event.webviewDestroyed | tg.Event.webviewProgress |
                              tg.Event.webviewConsoleMessage]:
                            if a.root is not None:
                                _dispatch_event_recursive(e, a.root)
                        case _:
                            pass
                if len(self.__activities) == 0:
                    return
    
    
    









