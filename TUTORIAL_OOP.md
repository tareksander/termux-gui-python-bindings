# Python Bindings OOP Tutorial
  
This is the tutorial for the object-oriented version of this library.  
Make sure you're familiar with the normal version a bit first, many things aren't explicitly repeated here.
  
Make sure you installed the library like explained in the README.  
This tutorial assumes you have the basic understanding of the Android GUI from the [crash course](https://github.com/termux/termux-gui).  
The full source code can also be found in the tutorial_oop folder.  
  
## Basic structure

Activities are now defined as classes, Layouts can be defined as classes for reusability,
the event loop is now build into the connection and with it comes an event system.  
You can also override the on_* methods of your Activity to catch Activity events.





```python
# Some classes like RemoteViews and Buffer are still required from termuxgui, so import both
import termuxgui.oo as tgo
import termuxgui as tg


# Layouts can be defined as classes, to make them reusable
class HelloWorldLayout(tgo.LinearLayout):
    def __init__(self, activity: tgo.Activity):
        # Initialize the LinearLayout as the root Layout
        super().__init__(activity)
        # define a TextView
        tgo.TextView(self.a, "Hello World", self)
        # define a Button
        b = tgo.Button(self.a, "Click me!", self)
        # Also new is the event system:
        # You can provide callables as on_* methods which will be called
        # if the corresponding Event is triggered on the View.
        # The methods get the event and the View as parameters.
        b.on_click = lambda e, v: print(e.type, e.value, v.id)


# Activities are now classes
class HelloWorldActivity(tgo.Activity):

    def __init__(self, c, t):
        super().__init__(c, t)
        # Add the Layout to the Activity
        HelloWorldLayout(self)


with tgo.Connection() as c:
    # Activities aren't created directly with the constructor anymore, but with the launch method of the connection
    c.launch(HelloWorldActivity)

    # The event loop is build into the connection.
    # It automatically quits if there aren't any Activities left.
    c.event_loop()
```

[helloworld.py](tutorial_oop/helloworld.py)<!-- @IGNORE PREVIOUS: link -->


