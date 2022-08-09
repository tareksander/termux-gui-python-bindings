#!/usr/bin/env python3

import base64
import sys
import termuxgui as tg


image = base64.standard_b64decode("""iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAFVUlEQVR4XtWaTUhtVRTHl1qZWpkg9mXhy8yejR6BRRMn0uRNUmgQcQfRoIiiSFQQIi1SauigDxokWvEcCBKiBBE9kohI571wpmaPNCuRlx/t1v/ss87Zd+/7sa/3nCMt+HGP96y91tpnr7U/zpWoeqlh6pibw89yYuqi7blJLXOT/WUotzH3MBdCcI3vCglswFZmUijwh5nnmY+Yb5lfmN+YP0Jwje9wDzrQRRtTMukIhl4ETzTHfMX8zagKQRu0hY0misX0kZhInsv1S8zPlB/Qv8ypJ9A128IWbEpNYDQSqw+zMB9nfqDYMYI5Dj/tJ1yOQm1hGz5EfCaFkmIaeJ05odi5XCcBbElHcA1fImfuhNnwA4qd4anZKZAEsAnb8jeKXaTiTpizweekDUr+2o6TxvTzBcW14N0Js3g+JNdoFpj+PqY4Jq/Cljn+NXKNZYnp9w3SYq8/jsgc3Ev5BWsbzwqzsJ8kLUXXCTPvZao0i+q8kBh+pDjGgiu2DM+LpBug92nMNpUiCySuXyEtTipJjxopXmGdeb6hoUGNjY2p1dXVgMXFRdXW1mY7TAOJ5RpzB2nJGwXpUY60YtG87+zsVDs7O+r09DRgenpaNTY2OnopIDG9QFqiUTCnJmyuoFQy9wcHB9Xu7m7QgcPDQzUyMuLopIDE9DXFTz+IXRaILop3lUVHANTX16upqSl1dHQUdGJra0v19fWpmpoaRzdBJCbE+ChpCWKXaQlDAwWvwm1paVErKytRKq2tran29nZHL2EktpdJSxC7jMAn4c2ST9+kq6tLbWxsBB04OTlRs7Ozqrm52dFLEIlthvK3+MEf31lKXuRyObW3txd04uDgQA0PD6eZShLb92RNpThd4chnKnlRV1enJiYmolTa399X/f39aXVCYttgWsiQ+5gdS8mb1tZWtbS0pI6Pj6N66O7udvQSQGLDGbuDDOlk9sKbFXcA9PT0qM3NzWgkZmZmVFNTk6NXJRIbXhQ8QoZgCv2/dUCm0kAeID0sppI355BC10lnTSQoiDMX8fj4+HkUcRsZUs+sWkpe2NMothUpBQ8kNmz3sfEMBPMp+NRSKou9kM3NzWW1kH1GehUO1gJcYCHDXhs3sVyX3U5gK7G8vBylzvr6etpbCTOuIdIx520lLjF/hgolR8HezG1vb2e5mfuLeYK0BCMg22msxt+EShVtp0dHRx0dk97eXjU/P+/F0NCQ0z5EYrrKNJOW6CggdfBqqFQ0jc5yoBkYGIj0y7GwsOC0Jzd9JN5I5IBwP+ljGxQTO1IivaRNOSYnJ532FMeCqb6DtDgHe/ToVmaMtHLRUcgYM463SMfoHOoh0iP8mvIT6QYlayEjJIZ1pp20FH3NiJ5hUXua+Yd0QyeVMkR8I5ZnSMdW9MWWCDpxJ/Mu6cYYvpLTakrAp6TOe6RjKpg6tshR7V7K/s20YPq7QjoWxOT1cheCesBQXWC+pNhwFulk+lhiHiT/n3DzBA2Qc9i24j29GM3qBw48+YdIx+CVOoVEirqjtrYWeXiD8p0l0RHb1g329T7p+b6q4EWQTreQzsNnKZ5iTedmwfkgE4P9EGD7OdK+4LPitCkmKB4YxMHnIj+htylesU2k+Mpht7vGNt/hzx7SPuDLu2ArERQThvVu5hI7xaqNzdU+uUGVA22uhjawE4ZNr3m+WpF9eANzF9PNXOZA3iRdeDgtYc/yK/N7CK7xHe5dCXUvk36zABuwBZvO/iZNgTMUGBzjnT0C6WAuMo8xfcxTIbjGd7gHHeiijZyqMg3cFowIgkDeAhkd/P/D7SG4lqcsOmhTdZ7/B+8oI+no0VGgAAAAAElFTkSuQmCC""")

with tg.Connection() as c:
    a = tg.Activity(c)
    
    root = tg.LinearLayout(a)
    
    normalb = tg.Button(a, "Normal notification", root)
    expandb = tg.Button(a, "Expandable notification", root)
    imgb = tg.Button(a, "Image notification", root)
    customb = tg.Button(a, "Custom notification", root)
    
    rv = tg.RemoteViews(c)
    cb = rv.addButton()
    rv.setText(cb, "Button")
    
    for ev in c.events():
        if ev.type == tg.Event.destroy:
            sys.exit()
        if ev.type == tg.Event.click:
            id = ev.value["id"]
            if id == normalb:
                # Create a new high priority notification in the channel "test"
                n = tg.Notification(c, "test", 3)
                # Set the text
                n.settitle("normal")
                n.setcontent("A normal text notification")
                # display it
                n.notify()
            if id == expandb:
                n = tg.Notification(c, "test", 3)
                n.settitle("expandable")
                # sets the expanded text
                n.setlargetext("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
                n.notify()
            if id == imgb:
                n = tg.Notification(c, "test", 3)
                n.settitle("image")
                n.setcontent("expand to see the image")
                # set the image, and display it as a thumbnail when the notification is collapsed
                n.setlargeimageasthumbnail(True)
                n.setlargeimage(image)
                n.notify()
            if id == customb:
                n = tg.Notification(c, "test", 3)
                # Set a custom layout for the notification
                n.setlayout(rv)
                n.notify()
        # catch the event from the button in the custom notification
        if ev.type == tg.Event.remoteclick:
            c.toast("notification button clicked", True)
