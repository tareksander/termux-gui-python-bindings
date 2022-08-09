#!/usr/bin/env python3

import sys
import termuxgui as tg
import time
import threading

with tg.Connection() as c:
    a = tg.Activity(c)
    
    root = tg.LinearLayout(a)
    
    # Create the TabLayout first, so it's at the top
    tabs = tg.TabLayout(a, root)
    
    # Set the tabs
    tabs.setlist(["Page 1", "Page 2", "Page 3"])
    
    tabs.setlinearlayoutparams(0)
    tabs.setheight(tg.View.WRAP_CONTENT)
    
    # Create a HorizontalScrollView without a visible scrollbar that snaps to the nearest item
    sv = tg.HorizontalScrollView(a, root, fillviewport=True, snapping=True, nobar=True)
    
    # wait until the activity is displayed and teh size is known
    while sv.getdimensions()[0] == 0:
        time.sleep(0.001)
    
    # Get the width one page should have
    pagew = sv.getdimensions()[0]
    
    # Create a horizontal layout
    svl = tg.LinearLayout(a, sv, vertical=False)
    
    # Create 3 pages
    page1 = tg.TextView(a, "Page 1", svl)
    page2 = tg.TextView(a, "Page 2", svl)
    page3 = tg.TextView(a, "Page 3", svl)
    
    # Set the width to one page-width
    page1.setwidth(pagew, True)
    page2.setwidth(pagew, True)
    page3.setwidth(pagew, True)
    
    # access to the gui objects has to be synchronized between threads
    conlcok = threading.Lock()
    
    tabselected = False
    tab = 0
    
    # create a thread to watch the scroll position and select the tab accordingly
    def watchscrollview():
        global tabselected
        while True:
            with conlcok:
                p = round(sv.getscrollposition()[0]/pagew)
                if not tabselected:
                    if p != tab:
                        tabs.selecttab(p)
                        tabselected = True
                elif p == tab:
                    tabselected = False
            time.sleep(0.01)
    threading.Thread(target=watchscrollview, daemon=True).start()
    
    # getting events needs no synchronisation...
    for ev in c.events():
        if ev.type == tg.Event.destroy:
            sys.exit()
        # TabLayout also emits an itemselected event, but has the tab index as the value
        if ev.type == tg.Event.itemselected and ev.value["id"] == tabs:
            # ...but calling any other method does
            with conlcok:
                tabselected = True
                tab = ev.value["selected"]
                # Scroll to the selected tab
                sv.setscrollposition(pagew*tab, 0, True)
