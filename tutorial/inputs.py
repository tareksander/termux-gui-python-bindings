#!/usr/bin/env python3

import termuxgui as tg
import sys
import time
from subprocess import run

ret = tg.connect()
if ret == None:
    sys.exit()
main, event = ret

a, t = tg.activity(main, dialog=True) # make this activity a dialog

layout = tg.createlinearlayout(main, a)

title = tg.createtextview(main, a, "Download Video", layout)
tg.settextsize(main, a, title, 30)

# Let's also create a small margin around the title so it looks nicer.
tg.setmargin(main, a, title, 5)


# For dialogs, we don't need to set "WRAP_CONTENT", in dialogs views are automatically packed as close as possible.

tv1 = tg.createtextview(main, a, "Video link:", layout)
et1 = tg.createedittext(main, a, "", layout)

tv2 = tg.createtextview(main, a, "Filename (empty for automatic filename):", layout)
et2 = tg.createedittext(main, a, "", layout)


# This creates an unchecked Checkbox
check = tg.createcheckbox(main, a, "high quality", False, layout)

# Create 2 buttons next to each other
buttons = tg.createlinearlayout(main, a, layout, True)

dl = tg.createbutton(main, a, "download", buttons)
cancel = tg.createbutton(main, a, "cancel", buttons)


hd = False

while True:
    ev = tg.getevent(event)
    if ev["type"] == "destroy" and ev["value"]["finishing"]:
        sys.exit()
    # Checkboxes also emit a click event when clicked, but they have the extra value "set" indicating whether the box is now checked or unchecked
    if ev["type"] == "click" and ev["value"]["id"] == check:
         hd = ev["value"]["set"]
    if ev["type"] == "click" and ev["value"]["id"] == dl:
        link = tg.gettext(main, a, et1)
        name = tg.gettext(main, a, et2)
        args = ["youtubedr", "download"]
        if len(name) != 0:
            args.extend(["-o", name])
        if hd:
            args.extend(["-q", "1080p"])
        args.append(link)
        if len(link) != 0:
            try:
                tg.finishactivity(main, a)
                run(args)
            except:
                pass
            tg.finishtask(main, t)
    if ev["type"] == "click" and ev["value"]["id"] == cancel:
        tg.finishactivity(main, a) # this handily also exits the program, because finishing the activity destroys it, and that event is send to us
