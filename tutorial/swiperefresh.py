#!/usr/bin/env python3

import termuxgui as tg
import sys

with tg.Connection() as c:
    a = tg.Activity(c)
    
    # Create a SwipeRefreshLayout as the root View
    ref = tg.SwipeRefreshLayout(a)
    
    # Add a LinearLayout as a child. A SwipeRefreshLayout can only have one child, so you should use a layout.
    layout = tg.LinearLayout(a, ref)
    
    
    refreshes = 0
    clicks = 0
    longclicks = 0
    
    tv1 = tg.TextView(a, "Refresh: "+str(refreshes), layout)
    tv2 = tg.TextView(a, "Clicks: "+str(clicks), layout)
    tv3 = tg.TextView(a, "Long clicks: "+str(longclicks), layout)
    
    # You can make other Views than Buttons send click events
    tv2.sendclickevent(True)
    
    # A long click event happens when you click a View and hold for a while
    tv3.sendlongclickevent(True)
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
        if ev.type == tg.Event.click:
            clicks += 1
            tv2.settext("Clicks: "+str(clicks))
        if ev.type == tg.Event.longClick:
            longclicks += 1
            tv3.settext("Long clicks: "+str(longclicks))
        if ev.type == tg.Event.refresh:
            refreshes += 1
            tv1.settext("Refresh: "+str(refreshes))
            # Set that we are done with refreshing, so that the animation stops and the gesture can trigger again
            ref.setrefreshing(False)
