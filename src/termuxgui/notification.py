import base64
from typing import Literal, List

from termuxgui.remoteviews import RemoteViews
from termuxgui.connection import Connection


class Notification:
    """This represents a notification."""

    def __init__(self, connection: Connection, channel: str, importance: Literal[0, 1, 2, 3, 4]):
        self.c = connection
        self.channel = channel
        self.importance = importance
        self.id = None
        self.ongoing = False
        self.layout = None
        self.expandedlayout = None
        self.hudlayout = None
        self.title = None
        self.content = None
        self.largeimage = None
        self.largetext = None
        self.largeimageasthumbnail = False
        self.icon = None
        self.alertonce = True
        self.showtimestamp = True
        self.timestamp = None
        self.actions = None

    def createchannel(self):
        """Creates the notification channel for the notification. This is called automatically when you call notify."""
        self.c.send_msg({"method": "createNotificationChannel", "params":
                        {"id": self.channel, "importance": self.importance, "name": self.channel}})
    
    def seticon(self, icon: bytes):
        """Set the icon of the notification.
        icon has to be a bytes object containing the icon in png or jpeg format."""
        self.icon = base64.standard_b64encode(icon).decode("ascii")
    
    def settitle(self, title: str):
        """Sets the title of the notification, removing any set custom layout."""
        self.title = title
        self.layout = None
        self.expandedlayout = None
        self.hudlayout = None
    
    def setcontent(self, content: str):
        """Sets the content of the notification, removing any set custom layout."""
        self.content = content
        self.layout = None
        self.expandedlayout = None
        self.hudlayout = None

    def setlargeimage(self, img: bytes):
        """Sets a large image for the notification, removing any set custom layout."""
        self.largeimage = base64.standard_b64encode(img).decode("ascii")
        self.layout = None
        self.expandedlayout = None
        self.hudlayout = None
        self.largetext = None

    def setlargetext(self, text: str):
        """Sets the text after expanding the notification, removing any set custom layout."""
        self.largetext = text
        self.layout = None
        self.expandedlayout = None
        self.hudlayout = None
        self.largeimage = None
    
    def setlayout(self, layout: RemoteViews):
        """Sets a custom layout for the notification.
        Removes any title, content largetext or largeimage."""
        self.layout = layout.rid
        self.largeimage = None
        self.largetext = None
        self.title = None
        self.content = None

    def setexpandedlayout(self, layout: RemoteViews):
        """Sets a custom expanded layout for the notification.
        Removes any title, content largetext or largeimage."""
        self.expandedlayout = layout.rid
        self.largeimage = None
        self.largetext = None
        self.title = None
        self.content = None

    def sethudlayout(self, layout: RemoteViews):
        """Sets a custom hud layout for the notification.
        Removes any title, content largetext or largeimage."""
        self.hudlayout = layout.rid
        self.largeimage = None
        self.largetext = None
        self.title = None
        self.content = None
    
    def setongoing(self, ongoing: bool):
        """Ongoing notifications can't be dismissed by the user."""
        self.ongoing = ongoing
    
    def setalertonce(self, alertonce: bool):
        """If you call notify more than once, whether to alert the user every time."""
        self.alertonce = alertonce
    
    def setshowtimestamp(self, show: bool):
        """Whether the timestamp is shown in the notification"""
        self.showtimestamp = show

    def settimestamp(self, timestamp: int):
        """Sets the timestamp of the notification. The format is the unix time in milliseconds."""
        self.timestamp = timestamp
    
    def setactions(self, actions: List[str]):
        """Sets the displayed actions for the notification."""
        self.actions = actions

    def setlargeimageasthumbnail(self, asthumbnail: bool):
        """Sets whether to show a large image as a thumbnail in the collapsed notification."""
        self.largeimageasthumbnail = asthumbnail
    
    def notify(self):
        """Creates/updates the notification."""
        args = {
            "ongoing": self.ongoing,
            "largeImageAsThumbnail": self.largeimageasthumbnail,
            "channel": self.channel,
            "importance": self.importance,
            "alertOnce": self.alertonce,
            "showTimestamp": self.showtimestamp,
        }
        if self.layout is not None:
            args["layout"] = self.layout
        if self.expandedlayout is not None:
            args["expandedLayout"] = self.expandedlayout
        if self.hudlayout is not None:
            args["hudLayout"] = self.hudlayout
        
        if self.title is not None:
            args["title"] = self.title
        if self.content is not None:
            args["content"] = self.content
        
        if self.largeimage is not None:
            args["largeImage"] = self.largeimage
        if self.largetext is not None:
            args["largeText"] = self.largetext

        if self.icon is not None:
            args["icon"] = self.icon

        if self.timestamp is not None:
            args["timestamp"] = self.timestamp

        if self.actions is not None:
            args["actions"] = self.actions
        
        if self.id is None:
            self.createchannel()
        else:
            args["id"] = self.id
        self.id = self.c.send_read_msg({"method": "createNotification", "params": args})

    def cancel(self):
        """Cancels the notification."""
        if self.id is not None:
            self.c.send_msg({"method": "cancelNotification", "params": {"id": self.id}})
