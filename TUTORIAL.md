# Python Bindings Tutorial
  
Make sure you installed the library like explained in the README.  
This tutorial assumes you have the basic understanding of the Android GUI from the [crash course](https://github.com/tareksander/termux-gui).  
The full source code can also be found in the tutorial folder.  
  
## Basic structure

```python
import sys

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
if ev.type == "destroy" and ev.value["finishing"]:
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
import sys
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

To use more than one View we need to use Layouts.  
The simplest Layout is LinearLayout.  
It displays it's children vertically or horizontally (vertically by default) and gives each child an equal part of the available space (by default again).  
Let's create a program with more views:
```python
import termuxgui as tg
import sys
import time

with tg.Connection() as c:
    
    a = tg.Activity(c)
    
    # For each View or Layout you create you can specify the parent Layout to create a hiearachy.
    # If you don't specify a parent, it will replace the current root View.
    # We first create a LinearLayout as our root View.
    root = tg.LinearLayout(a)
    
    # Then we create a TextView that we will use as a title
    title = tg.TextView(a, "Awesome Title", root)
    
    # We set the font size a bit bigger
    title.settextsize(30)
    
    
    contenttext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    # Now we create a TextView for the main content
    content = tg.TextView(a, contenttext, root)
    
    # And we add a Button at the end
    button = tg.Button(a, "Click here!", root)
    
    # Now we give the Layout priority to our content Textview so it is bigger than the Button and the title.
    content.setlinearlayoutparams(10)
    
    
    time.sleep(5)
```

[hellolayout.py](tutorial/hellolayout.py)<!-- @IGNORE PREVIOUS: link -->

## Events

But just displaying things is boring.  
Maybe we want to count the number of times the user could click the button in our Layout example an make a little game out of it.

```python
import termuxgui as tg
import sys
import time
import threading

with tg.Connection() as c:
    
    a = tg.Activity(c)
    
    # For each View or Layout you create you can specify the parent Layout to create a hiearachy.
    # If you don't specify a parent, it will replace the current root View.
    # We first create a LinearLayout as our root View.
    root = tg.LinearLayout(a)
    
    # Then we create a TextView that we will use as a title
    title = tg.TextView(a, "Awesome Title", root)
    
    # We set the font size a bit bigger
    title.settextsize(30)
    
    
    contenttext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    # Now we create a TextView for the main content
    content = tg.TextView(a, contenttext, root)
    
    # And we add a Button at the end
    button = tg.Button(a, "Click here!", root)
    
    # Now we give the Layout priority to our content Textview so it is bigger than the Button and the title.
    content.setlinearlayoutparams(10)
    
    count = 0
    
    # create a thread to handle the events, so we can still exit the program after 5 seconds no matter what
    def handleEvents():
        global count
        for ev in c.events(): # waits for events from the gui
            if ev.type == tg.Event.click: # checks for click events. We don't need to check the id, as there is only one Button in our example
                count = count + 1 
    watcher = threading.Thread(target=handleEvents,daemon=True)
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
```

The program will display the image you specified as a command line argument for 5 seconds in a small window.

[helloimage.py](tutorial/helloimage.py)<!-- @IGNORE PREVIOUS: link -->

## Advanced LinearLayout usage

Currently only LinearLayout is supported for laying out the Views on the screen.  
It's a simple Layout, but if you nest multiple LinearLayouts and configure them, it can be very flexible.  

It happens often that you want Views to only occupy the space they need in a LinearLayout instead of getting an equal share of the space.  

```python
import termuxgui as tg
import sys
import time
import threading
    
with tg.Connection() as c:
    a = tg.Activity(c)
    
    layout = tg.LinearLayout(a)
    
    # Create 3 TextViews
    tv1 = tg.TextView(a, "TextView 1", layout)
    tv2 = tg.TextView(a, "TextView 2", layout)
    tv3 = tg.TextView(a, "TextView 3", layout)
    
    
    # Now we make them only occupy the space they need.
    # We first have to set the Layout weight to 0 to prevent them from using the free space.
    tv1.setlinearlayoutparams(0)
    tv2.setlinearlayoutparams(0)
    tv3.setlinearlayoutparams(0)
    
    # Then we have to set the height to "WRAP_CONTENT".
    # You can specify width and height in 3 ways: as an integer in dp, "WRAP_CONTENT" and "MATCH_PARENT".
    # "WRAP_CONTENT" makes a View occupy only the space it needs.
    # "MATCH_PARENT" makes a view as large as the parent Layout in that dimension.
    
    # Since the TextViews are displayed in a list, we set the height to "WRAP_CONTENT".
    tv1.setheight("WRAP_CONTENT")
    tv2.setheight("WRAP_CONTENT")
    tv3.setheight("WRAP_CONTENT")
    
    time.sleep(5)
```

[linearlayout1.py](tutorial/linearlayout1.py)<!-- @IGNORE PREVIOUS: link -->  
  

Let's add a row of buttons and also make them as small as they need to be. 


```python
import termuxgui as tg
import sys
import time
import threading
    
with tg.Connection() as c:
    a = tg.Activity(c)
    
    layout = tg.LinearLayout(a)
    
    # Create 3 TextViews
    tv1 = tg.TextView(a, "TextView 1", layout)
    tv2 = tg.TextView(a, "TextView 2", layout)
    buttons = tg.LinearLayout(a, layout, False) # use False to create this as a horizontal Layout
    tv3 = tg.TextView(a, "TextView 3", layout)
    
    
    # Now we make them only occupy the space they need.
    # We first have to set the Layout weight to 0 to prevent them from using the free space.
    tv1.setlinearlayoutparams(0)
    tv2.setlinearlayoutparams(0)
    buttons.setlinearlayoutparams(0)
    tv3.setlinearlayoutparams(0)
    
    # Then we have to set the height to "WRAP_CONTENT".
    # You can specify width and height in 3 ways: as an integer in dp, "WRAP_CONTENT" and "MATCH_PARENT".
    # "WRAP_CONTENT" makes a View occupy only the space it needs.
    # "MATCH_PARENT" makes a view as large as the parent Layout in that dimension.
    
    # Since the TextViews are displayed in a list, we set the height to "WRAP_CONTENT".
    tv1.setheight("WRAP_CONTENT")
    tv2.setheight("WRAP_CONTENT")
    buttons.setheight("WRAP_CONTENT")
    tv3.setheight("WRAP_CONTENT")
    
    
    bt1 = tg.Button(a, "Button1", buttons)
    bt2 = tg.Button(a, "Button2", buttons)
    bt3 = tg.Button(a, "Button3", buttons)
    
    time.sleep(5)
```

As you can see, for nested LinearLayouts it is enough to set the height and weight of the nested Layout "WRAP_CONTENT" and 0.  


[linearlayout2.py](tutorial/linearlayout2.py)<!-- @IGNORE PREVIOUS: link -->  


## Inputs

Currently supported inputs are EditText, Button and Checkbox.  
Let's use our new LineaLayout knowledge to make a custom input dialog.  
The make it a practical example, we will make a dialog frontend for the `youtubedr` package to download videos.  
You can install that package if you want to try it out, but the UI works without that.  

```python
#!/usr/bin/env python3

import termuxgui as tg
import sys
import time
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







## More information

See the [protocol definition](https://github.com/tareksander/termux-gui/blob/main/Protocol.md) .


