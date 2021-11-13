#!/usr/bin/env python3

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
