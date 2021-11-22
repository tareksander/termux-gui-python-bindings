#!/usr/bin/env python3

import termuxgui as tg
import sys
import time
from subprocess import run

with tg.Connection() as c:
    a = tg.Activity(c, dialog=True)
    
    layout = tg.LinearLayout(a)
    
    title = tg.TextView(a, "Input Demo", layout)
    title.settextsize(30)
    title.setmargin(5)
    
    
    # Switches have a text displayed on the left and a switch that can be set on the right
    switch = tg.Switch(a, "Switch", layout)
    
    
    # ToggleButtons are more like Buttons, but have an on/off state, but you can't set the text
    tb = tg.ToggleButton(a, layout)
    
    
    # RadioGoups are containers for RadioButtons.
    # Inside a RadioGroup, only one RadioButton can be set.
    rg = tg.RadioGroup(a, layout)
    
    # The RadioButtons are created in a list, so you can check which of them is checked more easily
    rbs = [tg.RadioButton(a, "Radio 1", rg), tg.RadioButton(a, "Radio 2", rg), tg.RadioButton(a, "Radio 3", rg)]
    
    # Spinners display a drop-down menu with strings to choose from
    spinner = tg.Spinner(a, layout)
    
    strings = ["Option 1", "Option 2", "Option 3"]
    
    # You can set the list of values to choose from
    spinner.setlist(strings)
    
    for ev in c.events():
        if ev.type == tg.Event.destroy and ev.value["finishing"]:
            sys.exit()
        # Checked events work the same for Switches, ToggleButtons and Checkboxes
        if ev.type == tg.Event.click and ev.value["id"] == switch:
            print("Switch checked: ", ev.value["set"])
        if ev.type == tg.Event.click and ev.value["id"] == tb:
            print("ToggleButton checked: ", ev.value["set"])
        # A RadioGroup emits a selected event when a RadioButton is selected
        if ev.type == tg.Event.selected and ev.value["id"] == rg:
            # We can now use the index method of the list to find out which RadioButton is checked
            print("RadioButton checked: ", rbs.index(ev.value["selected"]))
        # Spinners evit an itemselected event
        if ev.type == tg.Event.itemselected and ev.value["id"] == spinner:
            # for itemselected events, selected is the selected value as a string
            print("Spinner selected: ", ev.value["selected"])
        
