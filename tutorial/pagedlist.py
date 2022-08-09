#!/usr/bin/env python3

import termuxgui as tg
import sys

with tg.Connection() as c:
    a = tg.Activity(c)
    
    # set the amount of items on each page
    pagesize = 20
    
    # generate content
    pagedcontent = []
    for i in range(1, 201):
        pagedcontent.append(f'Item {i}')
    
    page = 0
    
    # the paged list will be contained in this layout, and can be placed anywhere in the layout
    pagedlayout = tg.LinearLayout(a)
    
    # construct the controls at the top
    pagedcontrols = tg.LinearLayout(a, pagedlayout, vertical=False)
    pagedcontrols.setlinearlayoutparams(0)
    pagedcontrols.setheight(tg.View.WRAP_CONTENT)
    
    # buttons to go forward and back, and a display
    pagedback = tg.Button(a, "-", pagedcontrols)
    pagedpageview = tg.TextView(a, "1/1", pagedcontrols)
    pagedforward = tg.Button(a, "+", pagedcontrols)
    
    pagedback.setwidth(tg.View.WRAP_CONTENT)
    pagedforward.setwidth(tg.View.WRAP_CONTENT)
    
    pagedpageview.setmargin(5, "left")
    pagedpageview.setmargin(5, "right")
    
    # make the NestedScrollView for the content
    pagedscrollview = tg.NestedScrollView(a, pagedlayout)
    pagedscrollviewlayout = tg.LinearLayout(a, pagedscrollview)
    
    # Generate the Views for the content ahead of time, so the transition between pages
    # takes less time, and the user doesn't see a black flicker while the Views are removed
    pagedviews = []
    for i in range(0, pagesize):
        pagedviews.append(tg.TextView(a, "", pagedscrollviewlayout))
        pagedviews[i].settextsize(25)
    
    def topage(p: int):
        global page
        page = p
        # update the page indicator
        pagedpageview.settext(f"{p+1}/{int(len(pagedcontent)/pagesize)}")
        # set the new content
        for i in range(0, pagesize):
            pagedviews[i].settext(pagedcontent[p*pagesize+i])
    
    topage(0)
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
        if ev.type == tg.Event.click:
            if ev.value["id"] == pagedback and page > 0:
                topage(page-1)
            if ev.value["id"] == pagedforward and page < (len(pagedcontent)/pagesize)-1:
                topage(page+1)
