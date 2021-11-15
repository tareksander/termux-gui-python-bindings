#!/usr/bin/env python3

import termuxgui as tg
import sys
import time
from subprocess import run

with tg.Connection() as c:

    a = tg.Activity(c, dialog=True) # make this activity a dialog
    
    layout = tg.LinearLayout(a)
    
    title = tg.TextView(a, "Download Video", layout)
    title.settextsize(30)
    
    # Let's also create a small margin around the title so it looks nicer.
    title.setmargin(5)
    
    
    # For dialogs, we don't need to set "WRAP_CONTENT", in dialogs views are automatically packed as close as possible.
    
    tv1 = tg.TextView( a, "Video link:", layout)
    et1 = tg.EditText(a, "", layout)
    
    tv2 = tg.TextView( a, "Filename (empty for automatic filename):", layout)
    et2 = tg.EditText( a, "", layout)
    
    
    # This creates an unchecked Checkbox
    check = tg.Checkbox(a, "high quality", layout, False)
    
    # Create 2 buttons next to each other
    buttons = tg.LinearLayout(a, layout, False)
    
    dl = tg.Button(a, "download", buttons)
    cancel = tg.Button(a, "cancel", buttons)
    
    
    hd = False
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
        # Checkboxes also emit a click event when clicked, but they have the extra value "set" indicating whether the box is now checked or unchecked.
        # The id of the event is the View id. Comparing View object with view ids is supported and works as expected.
        if ev.type == tg.Event.click and ev.value["id"] == check:
            hd = ev.value["set"]
        if ev.type == tg.Event.click and ev.value["id"] == dl:
            link = et1.gettext()
            name = et2.gettext()
            args = ["youtubedr", "download"]
            if len(name) != 0:
                args.extend(["-o", name])
            if hd:
                args.extend(["-q", "1080p"])
            args.append(link)
            if len(link) != 0:
                try:
                    a.finish()
                    run(args)
                except:
                    pass
        if ev.type == tg.Event.click and ev.value["id"] == cancel:
            a.finish() # this handily also exits the program, because finishing the activity destroys it, and that event is send to us
