class Event:
    """This represents an Event in the GUI.

    The class variables are the available event types.

    Use ev.type == Event.eventtype to check for event types.

    ev.type contains the event type and ev.value is a dictionary containing the values of the event, if any."""

    # Event types
    # View events
    click = "click"
    longClick = "longClick"
    focusChange = "focusChange"
    key = "key"
    touch = "touch"
    refresh = "refresh"
    selected = "selected"  # used for RadioGroups
    itemselected = "itemselected"
    text = "text"
    notification = "notification"
    notificationDismissed = "notificationDismissed"
    notificationaction = "notificationaction"
    webviewNavigation = "webviewNavigation"
    webviewHTTPError = "webviewHTTPError"
    webviewError = "webviewError"
    webviewDestroyed = "webviewDestroyed"
    webviewProgress = "webviewProgress"
    webviewConsoleMessage = "webviewConsoleMessage"
    remoteclick = "remoteclick"

    # activity events
    create = "create"
    start = "start"
    resume = "resume"
    pause = "pause"
    stop = "stop"
    destroy = "destroy"
    userleavehint = "UserLeaveHint"
    pipchanged = "pipchanged"
    config = "config"
    back = "back"

    # general events
    screenon = "screen_on"
    screen_off = "screen_off"
    timezone = "timezone"
    locale = "locale"
    airplane = "airplane"

    # special overlay events
    overlaytouch = "overlayTouch"
    overlayScale = "overlayScale"

    # touch event action
    touch_up = "up"
    touch_down = "down"
    touch_pointer_up = "pointer_up"
    touch_pointer_down = "pointer_down"
    touch_cancel = "cancel"
    touch_move = "move"

    def __init__(self, ev: dict):
        self.type = ev["type"]
        self.value = {}
        try:
            self.value = ev["value"]
            if type(self.value) is dict:
                self.aid = self.value["aid"]
                self.id = self.value["id"]
        except KeyError:
            pass
