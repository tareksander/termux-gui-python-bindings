import termuxgui as tg
import sys
import time

with tg.Connection() as c:
    
    # create a new Activity. By default, a new Task as created.
    a = tg.Activity(c)
    # you can find the Task under a.t
    
    
    # create the TextView.
    tv = tg.TextView(a, "Hello world!")
    
    time.sleep(5)
    tv.settext("Goodbye world!")
    
    time.sleep(5)
