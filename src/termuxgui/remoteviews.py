import base64
from typing import Optional, Literal, Union

from termuxgui.connection import Connection


class RemoteViews:
    """This represents a remote Layout. You can use remote Layouts for custom notifications or widgets."""

    def __init__(self, connection: Connection):
        self.c = connection
        self.rid = self.c.send_read_msg({"method": "createRemoteLayout"})

    def __eq__(self, other):
        if type(other) is int:
            return self.rid == other
        if isinstance(other, RemoteViews):
            return self.rid == other.rid

    def delete(self):
        """Deletes this remote Layout."""
        self.c.send_msg({"method": "deleteRemoteLayout", "params": {"rid": self.rid}})

    def addFrameLayout(self, parent: Optional[int] = None) -> int:
        """Creates a FrameLayout in this remote Layout and returns the id, or -1 if it could not be created.
        The id can be used in further methods to manipulate the View."""
        args = {"rid": self.rid}
        if parent is not None:
            args["parent"] = parent
        return self.c.send_read_msg({"method": "addRemoteFrameLayout", "params": args})

    def addLinearLayout(self, parent: Optional[int] = None, vertical: Optional[bool] = None) -> int:
        """Creates a LinearLayout in this remote Layout and returns the id, or -1 if it could not be created.
        The id can be used in further methods to manipulate the View."""
        args = {"rid": self.rid}
        if vertical is not None:
            args["vertical"] = vertical
        if parent is not None:
            args["parent"] = parent
        return self.c.send_read_msg({"method": "addRemoteLinearLayout", "params": args})

    def addTextView(self, parent: Optional[int] = None) -> int:
        """Creates a TextView in this remote Layout and returns the id, or -1 if it could not be created.
        The id can be used in further methods to manipulate the View."""
        args = {"rid": self.rid}
        if parent is not None:
            args["parent"] = parent
        return self.c.send_read_msg({"method": "addRemoteTextView", "params": args})

    def addButton(self, parent: Optional[int] = None) -> int:
        """Creates a Button in this remote Layout and returns the id, or -1 if it could not be created.
        The id can be used in further methods to manipulate the View."""
        args = {"rid": self.rid}
        if parent is not None:
            args["parent"] = parent
        return self.c.send_read_msg({"method": "addRemoteButton", "params": args})

    def addImageView(self, parent: Optional[int] = None) -> int:
        """Creates an ImageView in this remote Layout and returns the id, or -1 if it could not be created.
        The id can be used in further methods to manipulate the View."""
        args = {"rid": self.rid}
        if parent is not None:
            args["parent"] = parent
        return self.c.send_read_msg({"method": "addRemoteImageView", "params": args})

    def addProgressBar(self, parent: Optional[int] = None) -> int:
        """Creates a ProgressBar in this remote Layout and returns the id, or -1 if it could not be created.
        The id can be used in further methods to manipulate the View."""
        args = {"rid": self.rid}
        if parent is not None:
            args["parent"] = parent
        return self.c.send_read_msg({"method": "addRemoteProgressBar", "params": args})

    def setBackgroundColor(self, id: int, color: int):
        """Sets the background color of a View in this remote Layout."""
        self.c.send_msg({"method": "setRemoteBackgroundColor", "params": {"rid": self.rid, "id": id, "color": color}})

    def setProgress(self, id: int, progress: int, max: int):
        """Sets the progress and maximum value of a ProgressBar in this remote Layout."""
        self.c.send_msg(
            {"method": "setRemoteProgressBar", "params": {"rid": self.rid, "id": id, "max": max, "progress": progress}})

    def setText(self, id: int, text: str):
        """Sets the text of a TextView in this remote Layout."""
        self.c.send_msg({"method": "setRemoteText", "params": {"rid": self.rid, "id": id, "text": text}})

    def setTextSize(self, id: int, size: int, px: bool):
        """Sets the text size of a TextView in this remote Layout.
        If px is true, the size will be in pixels. If not, it will be in dip."""
        self.c.send_msg({"method": "setRemoteTextSize", "params": {"rid": self.rid, "id": id, "size": size, "px": px}})

    def setTextColor(self, id: int, color: int):
        """Sets the text color of a TextView in this remote Layout."""
        self.c.send_msg({"method": "setRemoteTextColor", "params": {"rid": self.rid, "id": id, "color": color}})

    def setVisibility(self, id: int, vis: Literal[0, 1, 2]):
        """Sets the visibility of a View in this remote Layout.

        0 = gone, 1 = hidden, 2 = visible. While hidden, views are not visible but still take up space in the layout.
        Gone views do not take up layout space."""
        self.c.send_msg({"method": "setRemoteVisibility", "params": {"rid": self.rid, "id": id, "vis": vis}})

    def setPadding(self, id: int, left: int, top: int, right: int, bottom: int):
        """Sets the padding of a View in this remote Layout."""
        self.c.send_msg({"method": "setRemotePadding",
                         "params": {"rid": self.rid, "id": id, "left": left, "top": top, "right": right,
                                    "bottom": bottom}})

    def setImage(self, id: int, img: Union[str, bytes]):
        """Sets the image of an ImageView in this remote Layout.
        The image has to be a bytes object containing the image in png or jpeg format,
        or a string containing the base64 encoded version of it."""
        if isinstance(img, bytes):
            img = base64.standard_b64encode(img).decode("ascii")
        self.c.send_msg({"method": "setRemoteImage", "params": {"rid": self.rid, "id": id, "img": img}})

    def updateWidget(self, wid: str):
        """Sets the content of the Widget with ID wid to this remote Layout."""
        self.c.send_msg({"method": "setWidgetLayout", "params": {"rid": self.rid, "wid": wid}})
