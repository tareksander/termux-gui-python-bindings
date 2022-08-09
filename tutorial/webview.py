#!/usr/bin/env python3

import time
import termuxgui as tg
import sys

with tg.Connection() as c:
    a = tg.Activity(c)
    
    # create a WebView
    wv = tg.WebView(a)
    
    # Set the webpage content
    wv.setdata("<html> <body> <h1>Hello HTML</h1> <p>This is a paragraph</p> </body> </html>")
    
    time.sleep(3)
    
    # Load a web page via a URL
    wv.loaduri("https://www.google.com")
    
    time.sleep(3)
    
    # Prompt the user to allow Javascript
    wv.allowjavascript(True)
    
    # Run Javascript in the page
    wv.evaluatejs('''document.body.innerHTML = "<h1>Hello JS</h1> <p>Set via Javascript</p>"''')
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
