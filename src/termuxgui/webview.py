from typing import Optional, Literal

from termuxgui.activity import Activity
from termuxgui.view import View


class WebView(View):
    """This represents a WebView."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createWebView", "params": args}))

    def allowjavascript(self, allow: bool):
        """Sets whether Javascript execution is allowed in the WebView.
        If requesting to allow, the user is prompted and can deny the request.
        Blocks until the user responded.
        Returns wheter Javascript is enabled after the call."""
        self.a.c.send_read_msg({"method": "allowJavascript", "params": {"aid": self.a.aid, "id": self.id, "allow": allow}})

    def allowcontenturi(self, allow: bool):
        """Sets whether it is allowed to load content from a content:// URI."""
        self.a.c.send_msg({"method": "allowContentURI", "params": {"aid": self.a.aid, "id": self.id, "allow": allow}})

    def allownavigation(self, allow: bool):
        """Sets whether the user and Javascript are allowed to navigate to different sites."""
        self.a.c.send_msg({"method": "allowNavigation", "params": {"aid": self.a.aid, "id": self.id, "allow": allow}})

    def setdata(self, data: str):
        """Sets the document data."""
        self.a.c.send_msg({"method": "setData", "params": {"aid": self.a.aid, "id": self.id, "doc": data}})

    def loaduri(self, uri: str):
        """Loads a URI."""
        self.a.c.send_msg({"method": "loadURI", "params": {"aid": self.a.aid, "id": self.id, "uri": uri}})

    def goback(self):
        """Goes back in the history."""
        self.a.c.send_msg({"method": "goBack", "params": {"aid": self.a.aid, "id": self.id}})

    def goforward(self):
        """Goes forward in the history."""
        self.a.c.send_msg({"method": "goForward", "params": {"aid": self.a.aid, "id": self.id}})
    
    def evaluatejs(self, code: str):
        """Runs Javascript in the WebView, if Javascript is enabled."""
        self.a.c.send_msg({"method": "evaluateJS", "params": {"aid": self.a.aid, "id": self.id, "code": code}})
