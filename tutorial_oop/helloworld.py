#!/usr/bin/env python3

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
