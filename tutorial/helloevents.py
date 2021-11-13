#!/usr/bin/env python3

import termuxgui as tg
import sys
import time
import threading

ret = tg.connect()
if ret == None:
    sys.exit()
main, event = ret

a, t = tg.activity(main)

root = tg.createlinearlayout(main, a)

title = tg.createtextview(main, a, "Awesome Title", root)
tg.settextsize(main, a, title, 30)

contenttext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
content = tg.createtextview(main, a, contenttext, root)

button = tg.createbutton(main, a, "Click here!", root)

tg.setlinearlayoutparams(main, a, content, 10)

count = 0

# create a thread to handle the events, so we can still exit the program after 5 seconds no matter what
def handleEvents():
    global count
    while True:
        ev = tg.getevent(event) # waits for events from the gui
        if ev["type"] == "click": # checks for click events. We don't need to check the id, as there is only one Button in our example
            count = count + 1 
watcher = threading.Thread(target=handleEvents,daemon=True)
watcher.start()

time.sleep(5)
print("button pressed", count, "times")
