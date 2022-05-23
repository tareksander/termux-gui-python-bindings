#!/usr/bin/env python3

import time
from ctypes import *
from sdl2 import *
import sdl2.ext
import gc

import termuxgui as tg

with tg.Connection() as c:
    a = tg.Activity(c)
    time.sleep(0.5)  # wait for the activity to show

    im = tg.ImageView(a)

    # This create a pixel buffer with size 500x500
    b = tg.Buffer(c, 500, 500)

    # This sets the ImageView to display the buffer
    im.setbuffer(b)

    with b as mem:
        # This creates a c void pointer from the shared memory
        memp = cast(pointer(c_uint8.from_buffer(mem, 0)), c_void_p)

        # We initialize the video system of SDL
        SDL_Init(SDL_INIT_VIDEO)

        # Then we create a SDL surface from our buffer. We pass in the pointer to our buffer, the buffer width and
        # height, the bit depth (the format is always ARGB8888, so it's 32 bits), wthe pitch (bytes per row),
        # and the masks for the color values. The mask determines the format and is the same for all buffers
        surf = SDL_CreateRGBSurfaceFrom(memp, 500, 500, 32, 4 * 500, c_uint(0xff), c_uint(0xff00), c_uint(0xff0000),
                                        c_uint(0xff000000))

        # in general you would write:
        # SDL_CreateRGBSurfaceFrom(memp, width, height, 32, 4*width, c_uint(0xff), c_uint(0xff00), c_uint(0xff0000), c_uint(0xff000000))

        white = sdl2.ext.Color(255, 255, 255, 255)  # Color in RGBA format
        red = sdl2.ext.Color(255, 0, 0, 255)
        green = sdl2.ext.Color(0, 255, 0, 255)
        blue = sdl2.ext.Color(0, 0, 255, 255)

        for i in range(490):
            # clear the buffer
            sdl2.ext.fill(surf, white)

            # make a red square go from the top left to the bottom right
            sdl2.ext.fill(surf, red, (i, i, 10, 10))

            # make a green square go from the top right to the bottom left
            sdl2.ext.fill(surf, green, (490 - i, i, 10, 10))

            # make a blue square go from the top middle to the bottom middle
            sdl2.ext.fill(surf, blue, (245, i, 10, 10))

            # blit the shared memory buffer
            b.blit()
            # now we have to request that the ImageView redraws itself to reflect the new contents of the buffer
            im.refresh()

            time.sleep(0.01)

        # Make sure the shared memory can be closed
        del memp  # free the pointer
        gc.collect()  # let the garbage collector run, so the pointer is really discarded

        # do proper cleanup of SDL
        SDL_FreeSurface(surf)
        SDL_Quit()

        time.sleep(0.2)
