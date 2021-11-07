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
tg.settext(main, a, tv, "Goodbye world!")

time.sleep(5)
