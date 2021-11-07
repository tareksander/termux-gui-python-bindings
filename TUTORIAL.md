# Python Bindings Tutorial
  
Make sure you installed the library like explained in the README.  
This tutorial assumes you have the basic understanding of the Android GUI from the [crash course](https://github.com/tareksander/termux-gui).  
The full source code can be found in the tutorial folder.  
  
## Basic structure

```python
# you can also use from termuxgui import * to leave out the tg. to access methods 
import termuxgui as tg

import sys



ret = tg.connect()
if ret == None: # connection could not be established
    sys.exit()

# these are the sockets used to communicate with the plugin
main, event = ret


#  set up the gui
# ...

while True:
    ev = tg.getevent(event) # waits for events from the gui
    
    # react to events
```

After connecting to the plugin you can set up your gui.  
Then you have to wait for user input (or sleep for some time) and decide when to quit your program.  
If you only use one Activity you can use
```python
if ev["type"] == "destroy" and ev["value"]["finishing"]:
    sys.exit()
```
in the event loop to quit you program when the activity exits.


## Hello world

Let's first do a hello world.
We will display hello world in a new Activity and exit after 5 seconds.  

```python
import termuxgui as tg
import sys
import time

ret = tg.connect()
if ret == None:
    sys.exit()
main, event = ret

# create a new Activity.
# activity returns the Activity id and Task id that is used to refer to the new Activity and Task.
a, t = tg.activity(main)
# create the TextView.
# like activity, this returns an id that we can use to manipulate the TextView, but we won't do that in this example.
tv = tg.createtextview(main, a, "Hello world!")


time.sleep(5)
```

Now let's modify the example a bit: add 
```python
time.sleep(5)
tg.settext(main, a, t, "Goodbye world!")
```
after `tg.createtextview`.
Now it displays "Hello World!" for 5 seconds, "Goodbye world!" for 5 seconds and then exits.  
With that you just created your first dynamic layout.  
Congratulations!  






















































