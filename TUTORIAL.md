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
tg.settext(main, a, tv, "Goodbye world!")
```
after `tg.createtextview`.
Now it displays "Hello World!" for 5 seconds, "Goodbye world!" for 5 seconds and then exits.  
With that you just created your first dynamic layout.  
Congratulations!  


## Layout hierarchy

To use more than one View we need to use Layouts.  
The simplest Layout is LinearLayout.  
It displays it's children vertically or horizontally (vertically by default) and gives each child an equal part of the available space (by default again).  
Let's create a program with more views:
```python
import termuxgui as tg
import sys
import time

ret = tg.connect()
if ret == None:
    sys.exit()
main, event = ret

a, t = tg.activity(main)

# For each View or Layout you create you can specify the id of the parent Layout to create a hiearachy.
# If you don't specify a parent, it will replace the current root View.
# We first create a LinearLayout as our root View.
root = tg.createlinearlayout(main, a)

# Then we create a TextView that we will use as a title
title = tg.createtextview(main, a, "Awesome Title", root)

# We set the font size a bit bigger
tg.settextsize(main, a, title, 30)


contenttext = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
# Now we create a TextView for the main content
content = tg.createtextview(main, a, contenttext, root)

# And we add a Button at the end

button = tg.createbutton(main, a, "Click here!", root)


# Now we give the Layout priority to our content Textview so it is bigger than the Button and the title.
tg.setlinearlayoutparams(main, a, content, 10)



time.sleep(5)
```



## Events

But just displaying things is boring.  
Maybe we want to count the number of times the user could click the button in our Layout example an make a little game out of it.

```python
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
```

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

ret = tg.connect()
if ret == None:
    sys.exit()
main, event = ret

# specify that the Activity should be started in pip mode
a, t = tg.activity(main,pip=True)

# create an ImageView and set the image
iv = tg.createimageview(main, a)
tg.setimage(main, a, iv, image)

time.sleep(5)
```

The program will display the image you specified as a command line argument for 5 seconds in a small window.



























## More information

See the [protocol definition](https://github.com/tareksander/termux-gui/blob/main/Protocol.md) .


