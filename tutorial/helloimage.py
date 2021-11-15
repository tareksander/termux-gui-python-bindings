#!/usr/bin/env python3

import termuxgui as tg
import sys
import time
import threading
import io

image = None
with io.open(sys.argv[1], "rb") as f:
    image = f.read()
    
with tg.Connection() as c:
    a = tg.Activity(c, pip=True) # start the activity in picture-in-picture mode
    
    iv = tg.ImageView(a) # create a ImageView to display the image
    
    # Set the image
    iv.setimage(image)
    
    time.sleep(5)
