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
