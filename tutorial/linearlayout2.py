 #!/usr/bin/env python3

import termuxgui as tg
import sys
import time


ret = tg.connect()
if ret == None:
    sys.exit()
main, event = ret

a, t = tg.activity(main)



layout = tg.createlinearlayout(main, a)

# Create 3 TextViews
tv1 = tg.createtextview(main, a, "TextView 1", layout)
tv2 = tg.createtextview(main, a, "TextView 2", layout)
buttons = tg.createlinearlayout(main, a, layout, False) # use False to create this as a horizontal Layout
tv3 = tg.createtextview(main, a, "TextView 3", layout)

# Now we make them only occupy the space they need.
# We first have to set the Layout weight to 0 to prevent them from using the free space.
tg.setlinearlayoutparams(main, a, tv1, 0)
tg.setlinearlayoutparams(main, a, tv2, 0)
tg.setlinearlayoutparams(main, a, buttons, 0)
tg.setlinearlayoutparams(main, a, tv3, 0)

# Then we have to set the height to "WRAP_CONTENT".
# You can specify width and height in 3 ways: as an integer in dp, "WRAP_CONTENT" and "MATCH_PARENT".
# "WRAP_CONTENT" makes a View occupy only the space it needs.
# "MATCH_PARENT" makes a view as large as the parent Layout in that dimension.

# Since the TextViews are displayed in a list, we set the height to "WRAP_CONTENT".
tg.setheight(main, a, tv1, "WRAP_CONTENT")
tg.setheight(main, a, tv2, "WRAP_CONTENT")
tg.setheight(main, a, buttons, "WRAP_CONTENT")
tg.setheight(main, a, tv3, "WRAP_CONTENT")


tg.createbutton(main, a, "Button1", buttons)
tg.createbutton(main, a, "Button2", buttons)
tg.createbutton(main, a, "Button3", buttons)


time.sleep(5)
