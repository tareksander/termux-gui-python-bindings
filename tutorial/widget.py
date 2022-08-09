#!/usr/bin/env python3

import sys
import termuxgui as tg
import time
import os

with tg.Connection() as c:
    wid = sys.argv[1]
    # Create a remote layout
    rv = tg.RemoteViews(c)
    # Add a TextView
    tv = rv.addTextView()
    while True:
        files = os.listdir()
        files.sort()
        # Set the text
        rv.setText(tv, '\n'.join(files))
        # update the widget
        rv.updateWidget(wid)
        time.sleep(1)
