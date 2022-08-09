import base64
from typing import Optional, Literal

from termuxgui.buffer import Buffer
from termuxgui.activity import Activity
from termuxgui.view import View


class ImageView(View):
    """This represents an ImageView."""

    def __init__(self, activity: Activity, parent: Optional[View] = None,
                 visibility: Optional[Literal[0, 1, 2]] = None):
        args = {"aid": activity.aid, "visibility": visibility}
        if parent is not None:
            args["parent"] = parent.id
        View.__init__(self, activity, activity.c.send_read_msg({"method": "createImageView", "params": args}))

    def setimage(self, img: bytes):
        """Sets the image of the ImageView.
        The image has to be a bytes object containing the image in png or jpeg format."""
        self.a.c.send_msg({"method": "setImage", "params": {"aid": self.a.aid, "id": self.id,
                                                            "img": base64.standard_b64encode(img).decode("ascii")}})

    def setbuffer(self, b: Buffer):
        """Makes the ImageView use a shared buffer as the image source."""
        self.a.c.send_msg({"method": "setBuffer", "params": {"aid": self.a.aid, "id": self.id, "bid": b.bid}})

    def refresh(self):
        """Redraws the ImageView. You have to use this after blitting the Buffer when using a buffer."""
        self.a.c.send_msg({"method": "refreshImageView", "params": {"aid": self.a.aid, "id": self.id}})
