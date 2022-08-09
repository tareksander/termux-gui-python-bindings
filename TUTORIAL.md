# Python Bindings Tutorial
  
Make sure you installed the library like explained in the README.  
This tutorial assumes you have the basic understanding of the Android GUI from the [crash course](https://github.com/termux/termux-gui).  
The full source code can also be found in the tutorial folder.  
  
## Basic structure

```python

# you can also use from termuxgui import * to leave out the tg. to access methods and classes
import termuxgui as tg

# Create a connection to the plugin.
# Use with to automatically close the connection afterwards.
with tg.Connection() as c:
    
    
    #  set up the gui
    # ...
    
    for ev in c.events(): # wait for events from the gui
        
        
        # react to events
```

After connecting to the plugin you can set up your gui.  
Then you have to wait for user input (or sleep for some time) and decide when to quit your program.  
If you only use one Activity you can use
```python
if ev.type == tg.Event.destroy and ev.value["finishing"]:
    sys.exit()
```
in the event loop to quit you program when the activity exits.  
  
To make these examples shorter it is left out, but you should probably use this  

```python
try:
    import termuxgui as tg
except ModuleNotFoundError:
    sys.exit("termuxgui module not found. Please install the Termux:GUI python bindings: https://github.com/tareksander/termux-gui-python-bindings")
```

to import the library so users don't just see a useless ModuleNotFoundError when the library isn't installed.  
The library already throws a RuntimeError and prints out an informative message when it can't connect to the plugin.

## Hello world

Let's first do a hello world.
We will display hello world in a new Activity and exit after 5 seconds.  

```python
import termuxgui as tg
import time

with tg.Connection() as c:
    
    # create a new Activity. By default, a new Task as created.
    a = tg.Activity(c)
    # you can find the Task under a.t
    
    
    # create the TextView.
    tv = tg.TextView(a, "Hello world!")
    
    
    time.sleep(5)
```

Now let's modify the example a bit: add 
```python
time.sleep(5)
tv.settext(main, a, tv, "Goodbye world!")
```
after `tv = tg.TextView(a, "Hello world!")`.
Now it displays "Hello World!" for 5 seconds, "Goodbye world!" for 5 seconds and then exits.  
With that you just created your first dynamic layout.  
Congratulations!  

[helloworld.py](tutorial/helloworld.py)<!-- @IGNORE PREVIOUS: link -->

## Layout hierarchy

To use more than one View we need to use layouts.  
The simplest layout is LinearLayout.  
It displays its children vertically or horizontally (vertically by default) and gives each child an equal part of the available space (by default again).  
Let's create a program with more views:
```python
import termuxgui as tg
import time

with tg.Connection() as c:
    a = tg.Activity(c)
    
    # For each View or Layout you create you can specify the parent layout to create a hierarchy.
    # If you don't specify a parent, it will replace the current root View.
    # We first create a LinearLayout as our root View.
    root = tg.LinearLayout(a)
    
    # Then we create a TextView that we will use as a title
    title = tg.TextView(a, "Awesome Title", root)
    
    # We set the font size a bit bigger
    title.settextsize(30)
    
    contenttext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor "\
                  "invidunt utlabore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et "\
                  "accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "\
                  "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur "\
                  "sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore "\
                  "magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo "\
                  "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est "\
                  "Lorem ipsum dolor sit amet."
    # Now we create a TextView for the main content
    content = tg.TextView(a, contenttext, root)
    
    # And we add a Button at the end
    button = tg.Button(a, "Click here!", root)
    
    # Now we give the Layout priority to our content Textview, so it is bigger than the Button and the title.
    content.setlinearlayoutparams(10)
    
    time.sleep(5)
```

[hellolayout.py](tutorial/hellolayout.py)<!-- @IGNORE PREVIOUS: link -->

## Events

But just displaying things is boring.  
Maybe we want to count the number of times the user could click the button in our Layout example and make a little game out of it.

```python
import termuxgui as tg
import time
import threading

with tg.Connection() as c:
    a = tg.Activity(c)
    
    # For each View or Layout you create you can specify the parent Layout to create a hierarchy.
    # If you don't specify a parent, it will replace the current root View.
    # We first create a LinearLayout as our root View.
    root = tg.LinearLayout(a)
    
    # Then we create a TextView that we will use as a title
    title = tg.TextView(a, "Awesome Title", root)
    
    # We set the font size a bit bigger
    title.settextsize(30)
    
    contenttext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "\
                  "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At "\
                  "vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, "\
                  "no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit "\
                  "amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut "\
                  "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam "\
                  "et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "\
                  "sanctus est Lorem ipsum dolor sit amet."
    # Now we create a TextView for the main content
    content = tg.TextView(a, contenttext, root)
    
    # And we add a Button at the end
    button = tg.Button(a, "Click here!", root)
    
    # Now we give the layout priority to our content Textview so it is bigger than the Button and the title.
    content.setlinearlayoutparams(10)
    
    count = 0
    
    # create a thread to handle the events, so we can still exit the program after 5 seconds no matter what
    def handleEvents():
        global count
        for ev in c.events():  # waits for events from the gui
            # checks for click events. We don't need to check the id, as there is only one Button in our example
            if ev.type == tg.Event.click:
                count = count + 1
    
    
    watcher = threading.Thread(target=handleEvents, daemon=True)
    watcher.start()
    
    time.sleep(5)
    print("button pressed", count, "times")
```

[helloevents.py](tutorial/helloevents.py)<!-- @IGNORE PREVIOUS: link -->

## Picture-in-picture and images

Now let's make something you would actually want to use:  
A terminal image viewer.  
You can set a png or jpeg directly as the image of an ImageView.  
With picture-in-picture mode you can display an Activity in a small window.

```python
import termuxgui as tg
import sys
import time
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
```

The program will display the image you specified as a command line argument for 5 seconds in a small window.

[helloimage.py](tutorial/helloimage.py)<!-- @IGNORE PREVIOUS: link -->

## Advanced LinearLayout usage

Currently only LinearLayout is supported for laying out the Views on the screen.  
It's a simple Layout, but if you nest multiple LinearLayouts and configure them, it can be very flexible.  

It happens often that you want Views to only occupy the space they need in a LinearLayout instead of getting an equal share of the space.  

```python
import termuxgui as tg
import time
    
with tg.Connection() as c:
    a = tg.Activity(c)
    
    layout = tg.LinearLayout(a)
    
    # Create 3 TextViews
    tv1 = tg.TextView(a, "TextView 1", layout)
    tv2 = tg.TextView(a, "TextView 2", layout)
    tv3 = tg.TextView(a, "TextView 3", layout)
    
    
    # Now we make them only occupy the space they need.
    # We first have to set the layout weight to 0 to prevent them from using the free space.
    tv1.setlinearlayoutparams(0)
    tv2.setlinearlayoutparams(0)
    tv3.setlinearlayoutparams(0)
    
    # Then we have to set the height to "WRAP_CONTENT".
    # You can specify width and height in 3 ways: as an integer in dp, "WRAP_CONTENT" and "MATCH_PARENT".
    # "WRAP_CONTENT" makes a View occupy only the space it needs.
    # "MATCH_PARENT" makes a view as large as the parent Layout in that dimension.
    # To prevent mistyping, "WRAP_CONTENT" and "MATCH_PARENT" are also defined as constants in the View class.
    
    # Since the TextViews are displayed in a list, we set the height to "WRAP_CONTENT".
    tv1.setheight(tg.View.WRAP_CONTENT)
    tv2.setheight(tg.View.WRAP_CONTENT)
    tv3.setheight(tg.View.WRAP_CONTENT)
    
    time.sleep(5)
```

[linearlayout1.py](tutorial/linearlayout1.py)<!-- @IGNORE PREVIOUS: link -->  
  

Let's add a row of buttons and also make them as small as they need to be. 


```python
import termuxgui as tg
import time
    
with tg.Connection() as c:
    a = tg.Activity(c)
    
    layout = tg.LinearLayout(a)
    
    # Create 3 TextViews
    tv1 = tg.TextView(a, "TextView 1", layout)
    tv2 = tg.TextView(a, "TextView 2", layout)
    buttons = tg.LinearLayout(a, layout, False) # use False to create this as a horizontal layout
    tv3 = tg.TextView(a, "TextView 3", layout)
    
    
    # Now we make them only occupy the space they need.
    # We first have to set the layout weight to 0 to prevent them from using the free space.
    tv1.setlinearlayoutparams(0)
    tv2.setlinearlayoutparams(0)
    buttons.setlinearlayoutparams(0)
    tv3.setlinearlayoutparams(0)
    
    # Then we have to set the height to "WRAP_CONTENT".
    # You can specify width and height in 3 ways: as an integer in dp, "WRAP_CONTENT" and "MATCH_PARENT".
    # "WRAP_CONTENT" makes a View occupy only the space it needs.
    # "MATCH_PARENT" makes a view as large as the parent layout in that dimension.
    
    # Since the TextViews are displayed in a list, we set the height to "WRAP_CONTENT".
    tv1.setheight(tg.View.WRAP_CONTENT)
    tv2.setheight(tg.View.WRAP_CONTENT)
    buttons.setheight(tg.View.WRAP_CONTENT)
    tv3.setheight(tg.View.WRAP_CONTENT)
    
    
    bt1 = tg.Button(a, "Button1", buttons)
    bt2 = tg.Button(a, "Button2", buttons)
    bt3 = tg.Button(a, "Button3", buttons)
    
    time.sleep(5)
```

As you can see, for nested LinearLayouts it is enough to set the height and weight of the nested Layout to tg.View.WRAP_CONTENT and 0.  


[linearlayout2.py](tutorial/linearlayout2.py)<!-- @IGNORE PREVIOUS: link -->  


## Inputs

Currently supported inputs are EditText, Button and Checkbox.  
Let's use our new LineaLayout knowledge to make a custom input dialog.  
The make it a practical example, we will make a dialog frontend for the `youtubedr` package to download videos.  
You can install that package if you want to try it out, but the UI works without that.  

```python
import termuxgui as tg
import sys
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
```


[inputs.py](tutorial/inputs.py)<!-- @IGNORE PREVIOUS: link -->  
<br>
<br>

  
There are some more Views you can use to get user input:  


```python
import termuxgui as tg
import sys

with tg.Connection() as c:
    a = tg.Activity(c, dialog=True)
    
    layout = tg.LinearLayout(a)
    
    title = tg.TextView(a, "Input Demo", layout)
    title.settextsize(30)
    title.setmargin(5)
    
    # Switches have a text displayed on the left and a switch that can be set on the right
    switch = tg.Switch(a, "Switch", layout)
    
    # ToggleButtons are more like Buttons, but have an on/off state, but you can't set the text
    tb = tg.ToggleButton(a, layout)
    
    # RadioGoups are containers for RadioButtons.
    # Inside a RadioGroup, only one RadioButton can be set.
    rg = tg.RadioGroup(a, layout)
    
    # The RadioButtons are created in a list, so you can check which of them is checked more easily
    rbs = [tg.RadioButton(a, "Radio 1", rg), tg.RadioButton(a, "Radio 2", rg), tg.RadioButton(a, "Radio 3", rg)]
    
    # Spinners display a drop-down menu with strings to choose from
    spinner = tg.Spinner(a, layout)
    
    strings = ["Option 1", "Option 2", "Option 3"]
    
    # You can set the list of values to choose from
    spinner.setlist(strings)
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
        # Checked events work the same for Switches, ToggleButtons and Checkboxes
        if ev.type == tg.Event.click and ev.value["id"] == switch:
            print("Switch checked: ", ev.value["set"])
        if ev.type == tg.Event.click and ev.value["id"] == tb:
            print("ToggleButton checked: ", ev.value["set"])
        # A RadioGroup emits a selected event when a RadioButton is selected
        if ev.type == tg.Event.selected and ev.value["id"] == rg:
            # We can now use the index method of the list to find out which RadioButton is checked
            print("RadioButton checked: ", rbs.index(ev.value["selected"]))
        # Spinners emit an itemselected event
        if ev.type == tg.Event.itemselected and ev.value["id"] == spinner:
            # for itemselected events, selected is the selected value as a string
            print("Spinner selected: ", ev.value["selected"])
```

[inputs2.py](tutorial/inputs2.py)<!-- @IGNORE PREVIOUS: link -->  

## Buffers

You can use a shared memory buffer to draw to ImageViews without having to convert it to an image file first or even sending the data.  
Using a shared buffer is much faster than setting the image for an ImageView every time.  
  
This example uses SDL2 and a python wrapper to draw to the buffer.  
You can install both using

    pkg install x11-repo
    pkg install sdl2
    pip install pysdl2

You might need to do

    export PYSDL2_DLL_PATH=$PREFIX/lib

for pysdl2 to find the sdl2 library.

```python
import time
from ctypes import *
from sdl2 import *
import sdl2.ext
import gc

import termuxgui as tg

with tg.Connection() as c:
    
    a = tg.Activity(c)
    time.sleep(0.5) # wait for the activity to show
    
    im = tg.ImageView(a)
    
    # This create a pixel buffer with size 500x500
    b = tg.Buffer(c, 500,500)
    
    # This sets the ImageView to display the buffer
    im.setbuffer(b)
    
    
    with b as mem:
        # This creates a c void pointer from the shared memory
        memp = cast(pointer(c_uint8.from_buffer(mem, 0)), c_void_p)
        
        # We initialize the video system of SDL
        SDL_Init(SDL_INIT_VIDEO)
        
        # Then we create a SDL surface from our buffer. We pass in the pointer to our buffer, the buffer width and height,
        # the bit depth (the format is always ARGB8888, so it's 32 bits), wthe pitch (bytes per row), and the masks for the color values.
        # The mask determines the format and is the same for all buffers
        surf = SDL_CreateRGBSurfaceFrom(memp, 500, 500, 32, 4*500, c_uint(0xff), c_uint(0xff00), c_uint(0xff0000), c_uint(0xff000000))
        
        # in general you would write:
        # SDL_CreateRGBSurfaceFrom(memp, width, height, 32, 4*width, c_uint(0xff), c_uint(0xff00), c_uint(0xff0000), c_uint(0xff000000))
        
        
        white = sdl2.ext.Color(255, 255, 255, 255) # Color in RGBA format
        red = sdl2.ext.Color(255, 0, 0, 255)
        green = sdl2.ext.Color(0, 255, 0, 255)
        blue = sdl2.ext.Color(0, 0, 255, 255)
        
        
        for i in range(490):
            
            # clear the buffer
            sdl2.ext.fill(surf, white)
            
            # make a red square go from the top left to the bottom right
            sdl2.ext.fill(surf, red, (i,i,10,10))
            
            # make a green square go from the top right to the bottom left
            sdl2.ext.fill(surf, green, (490-i,i,10,10))
            
            # make a blue square go from the top middle to the bottom middle
            sdl2.ext.fill(surf, blue, (245,i,10,10))
            
            
            
            # and blit the shared memory buffer
            b.blit()
            # now we have to request that the ImageView redraws itself to reflect the new contents of the buffer
            im.refresh()
            
            time.sleep(0.01)
        
        # Make sure the shared memory can be closed
        del memp # free the pointer
        gc.collect() # let the garbage collector run, so the pointer is really discarded
        
        
        # do proper cleanup of SDL
        SDL_FreeSurface(surf)
        SDL_Quit()
        
        time.sleep(0.2)
```

[buffers.py](tutorial/buffers.py)<!-- @IGNORE PREVIOUS: link -->  


## SwipeRefreshLayout and more events

SwipeRefreshLayout enables you to use the swipe-to-refresh gesture.  
When a refresh gesture is detected, an event is fired.  
This is a good opportunity to also introduce more events.  


```python
import termuxgui as tg
import sys

with tg.Connection() as c:
    a = tg.Activity(c)
    
    # Intercept the back button. Instead of finishing the Activity, it now sends an event instead
    a.interceptbackbutton(True)
    # Also possible: a = tg.Activity(c, intercept=True)
    
    # Create a SwipeRefreshLayout as the root View
    ref = tg.SwipeRefreshLayout(a)
    
    # Add a LinearLayout as a child. A SwipeRefreshLayout can only have one child, so you should use a layout.
    layout = tg.LinearLayout(a, ref)
    
    
    refreshes = 0
    clicks = 0
    longclicks = 0
    
    tv1 = tg.TextView(a, "Refresh: " + str(refreshes), layout)
    tv2 = tg.TextView(a, "Clicks: " + str(clicks), layout)
    tv3 = tg.TextView(a, "Long clicks: " + str(longclicks), layout)
    
    # You can make other Views than Buttons send click events
    tv2.sendclickevent(True)
    
    # A long click event happens when you click a View and hold for a while
    tv3.sendlongclickevent(True)
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
        if ev.type == tg.Event.click:
            clicks += 1
            tv2.settext("Clicks: " + str(clicks))
        if ev.type == tg.Event.longClick:
            longclicks += 1
            tv3.settext("Long clicks: " + str(longclicks))
        if ev.type == tg.Event.refresh:
            refreshes += 1
            tv1.settext("Refresh: " + str(refreshes))
            # Set that we are done with refreshing, so that the animation stops and the gesture can trigger again
            ref.setrefreshing(False)
        # Back button presses generate an event now
        if ev.type == tg.Event.back:
            c.toast("User pressed the back button", True)
```


[swiperefresh.py](tutorial/swiperefresh.py)<!-- @IGNORE PREVIOUS: link -->  


# Widgets

After putting a widget on the homescreen, the user gets a chance to copy the generated id.
You can use this id to update the widget.  
  
This example updates a widget with the contents of the directory it's started in and receives the widget id as a parameter.

````python
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
````

[widget.py](tutorial/widget.py)<!-- @IGNORE PREVIOUS: link -->

## Notifications

Notifications are also supported, so you don't need to adapt Termux:API notifications.  
In addition, you can also construct notifications from RemoteViews, just like widgets.  
This example only shows some methods of Notification, you can look up the rest in the documentation if you need them.

````python
import base64
import sys
import termuxgui as tg


image = base64.standard_b64decode("""iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAFVUlEQVR4XtWaTUhtVRTHl1qZWpkg9mXhy8yejR6BRRMn0uRNUmgQcQfRoIiiSFQQIi1SauigDxokWvEcCBKiBBE9kohI571wpmaPNCuRlx/t1v/ss87Zd+/7sa/3nCMt+HGP96y91tpnr7U/zpWoeqlh6pibw89yYuqi7blJLXOT/WUotzH3MBdCcI3vCglswFZmUijwh5nnmY+Yb5lfmN+YP0Jwje9wDzrQRRtTMukIhl4ETzTHfMX8zagKQRu0hY0misX0kZhInsv1S8zPlB/Qv8ypJ9A128IWbEpNYDQSqw+zMB9nfqDYMYI5Dj/tJ1yOQm1hGz5EfCaFkmIaeJ05odi5XCcBbElHcA1fImfuhNnwA4qd4anZKZAEsAnb8jeKXaTiTpizweekDUr+2o6TxvTzBcW14N0Js3g+JNdoFpj+PqY4Jq/Cljn+NXKNZYnp9w3SYq8/jsgc3Ev5BWsbzwqzsJ8kLUXXCTPvZao0i+q8kBh+pDjGgiu2DM+LpBug92nMNpUiCySuXyEtTipJjxopXmGdeb6hoUGNjY2p1dXVgMXFRdXW1mY7TAOJ5RpzB2nJGwXpUY60YtG87+zsVDs7O+r09DRgenpaNTY2OnopIDG9QFqiUTCnJmyuoFQy9wcHB9Xu7m7QgcPDQzUyMuLopIDE9DXFTz+IXRaILop3lUVHANTX16upqSl1dHQUdGJra0v19fWpmpoaRzdBJCbE+ChpCWKXaQlDAwWvwm1paVErKytRKq2tran29nZHL2EktpdJSxC7jMAn4c2ST9+kq6tLbWxsBB04OTlRs7Ozqrm52dFLEIlthvK3+MEf31lKXuRyObW3txd04uDgQA0PD6eZShLb92RNpThd4chnKnlRV1enJiYmolTa399X/f39aXVCYttgWsiQ+5gdS8mb1tZWtbS0pI6Pj6N66O7udvQSQGLDGbuDDOlk9sKbFXcA9PT0qM3NzWgkZmZmVFNTk6NXJRIbXhQ8QoZgCv2/dUCm0kAeID0sppI355BC10lnTSQoiDMX8fj4+HkUcRsZUs+sWkpe2NMothUpBQ8kNmz3sfEMBPMp+NRSKou9kM3NzWW1kH1GehUO1gJcYCHDXhs3sVyX3U5gK7G8vBylzvr6etpbCTOuIdIx520lLjF/hgolR8HezG1vb2e5mfuLeYK0BCMg22msxt+EShVtp0dHRx0dk97eXjU/P+/F0NCQ0z5EYrrKNJOW6CggdfBqqFQ0jc5yoBkYGIj0y7GwsOC0Jzd9JN5I5IBwP+ljGxQTO1IivaRNOSYnJ532FMeCqb6DtDgHe/ToVmaMtHLRUcgYM463SMfoHOoh0iP8mvIT6QYlayEjJIZ1pp20FH3NiJ5hUXua+Yd0QyeVMkR8I5ZnSMdW9MWWCDpxJ/Mu6cYYvpLTakrAp6TOe6RjKpg6tshR7V7K/s20YPq7QjoWxOT1cheCesBQXWC+pNhwFulk+lhiHiT/n3DzBA2Qc9i24j29GM3qBw48+YdIx+CVOoVEirqjtrYWeXiD8p0l0RHb1g329T7p+b6q4EWQTreQzsNnKZ5iTedmwfkgE4P9EGD7OdK+4LPitCkmKB4YxMHnIj+htylesU2k+Mpht7vGNt/hzx7SPuDLu2ArERQThvVu5hI7xaqNzdU+uUGVA22uhjawE4ZNr3m+WpF9eANzF9PNXOZA3iRdeDgtYc/yK/N7CK7xHe5dCXUvk36zABuwBZvO/iZNgTMUGBzjnT0C6WAuMo8xfcxTIbjGd7gHHeiijZyqMg3cFowIgkDeAhkd/P/D7SG4lqcsOmhTdZ7/B+8oI+no0VGgAAAAAElFTkSuQmCC""")

with tg.Connection() as c:
    a = tg.Activity(c)
    
    root = tg.LinearLayout(a)
    
    normalb = tg.Button(a, "Normal notification", root)
    expandb = tg.Button(a, "Expandable notification", root)
    imgb = tg.Button(a, "Image notification", root)
    customb = tg.Button(a, "Custom notification", root)
    
    rv = tg.RemoteViews(c)
    cb = rv.addButton()
    rv.setText(cb, "Button")
    
    for ev in c.events():
        if ev.type == tg.Event.destroy:
            sys.exit()
        if ev.type == tg.Event.click:
            id = ev.value["id"]
            if id == normalb:
                # Create a new high priority notification in the channel "test"
                n = tg.Notification(c, "test", 3)
                # Set the text
                n.settitle("normal")
                n.setcontent("A normal text notification")
                # display it
                n.notify()
            if id == expandb:
                n = tg.Notification(c, "test", 3)
                n.settitle("expandable")
                # sets the expanded text
                n.setlargetext("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
                n.notify()
            if id == imgb:
                n = tg.Notification(c, "test", 3)
                n.settitle("image")
                n.setcontent("expand to see the image")
                # set the image, and display it as a thumbnail when the notification is collapsed
                n.setlargeimageasthumbnail(True)
                n.setlargeimage(image)
                n.notify()
            if id == customb:
                n = tg.Notification(c, "test", 3)
                # Set a custom layout for the notification
                n.setlayout(rv)
                n.notify()
        # catch the event from the button in the custom notification
        if ev.type == tg.Event.remoteclick:
            c.toast("notification button clicked", True)
````

[notify.py](tutorial/notify.py)<!-- @IGNORE PREVIOUS: link -->


## WebView

WebViews can be used to display HTML or web pages in a layout.  
There have been many vulnerabilities in the Android WebView, so the default settings are to make it more secure:
- Javascript is disabled
- The user or Javascript can't navigate, the client has to do it

You should never load untrusted data into the WebView, especially not with Javascript enabled.
Blocking the navigation helps with that, because you can set a trusted website and be sure it can't be navigated away from.



````python
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
````



## Design patterns

Here are some patterns for combining Views into larger pieces.

### Navigable pages

You can use NestedScrollView to create pages you can swipe through, and optionally use a TabLayout to navigate.

````python
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
````

[pages.py](tutorial/pages.py)<!-- @IGNORE PREVIOUS: link -->



### Paged lists

Because endless scrolling is hard to implement, consider paged lists instead.  
This example implements a paged list to display content.

````python
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
    pagedpageview.setgravity(1, 1)  # Center the text
    
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
````



## More information

See the [protocol definition](https://github.com/tareksander/termux-gui/blob/main/Protocol.md) and the [documentation](https://tareksander.github.io/termux-gui-python-bindings/termuxgui/index.html) for this library.


