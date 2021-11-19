"""This is a library for interacting with the Termux:GUI plugin from python.

You don't need to include all the submodules, all needed classes are automatically included in the package scope upon importing the package.
"""

__all__ = ["Activity", "Connection", "Event", "Task", "View", "ViewGroup", "LinearLayout",
           "FrameLayout", "Space", "TextView", "EditText", "ImageView", "Button",
           "Checkbox", "NestedScrollView", "Buffer", "RadioGroup", "RadioButton", "Spinner", "ToggleButton", "Switch", "CompoundButton"]


for m in __all__:
    exec("from termuxgui."+m.lower()+" import "+m)
del m


