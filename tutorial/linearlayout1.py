#!/usr/bin/env python3

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
