__all__ = ["Activity", "Connection", "Event", "Task", "View", "ViewGroup", "LinearLayout",
           "FrameLayout", "Space", "TextView", "EditText", "ImageView", "Button",
           "Checkbox", "NestedScrollView", "Buffer"]


for m in __all__:
    exec("from termuxgui."+m.lower()+" import "+m)
del m


