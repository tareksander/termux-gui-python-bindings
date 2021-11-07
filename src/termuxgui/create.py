from json import dumps

from termuxgui.__send_read_msg  import __send_read_msg


def createlinearlayout(mainSocket, aid, parent=None):
    args = {"aid": aid}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createLinearLayout", "params": args}))

def createframelayout(mainSocket, aid, parent=None):
    args = {"aid": aid}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createFrameLayout", "params": args}))


def createspace(mainSocket, aid, parent=None):
    args = {"aid": aid}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createSpace", "params": args}))


def createtextview(mainSocket, aid, text, parent=None):
    args = {"aid": aid, "text": text}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createTextView", "params": args}))


def createedittext(mainSocket, aid, text, parent=None):
    args = {"aid": aid, "text": text}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createEditText", "params": args}))

def createbutton(mainSocket, aid, text, parent=None):
    args = {"aid": aid, "text": text}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createButton", "params": args}))


def createcheckbox(mainSocket, aid, checked=False, parent=None):
    args = {"aid": aid, "checked": checked}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createCheckbox", "params": args}))


def createnestedscrollview(mainSocket, aid, parent=None):
    args = {"aid": aid}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createNestedScrollView", "params": args}))


def createimageview(mainSocket, aid, parent=None):
    args = {"aid": aid}
    if parent != None:
        args["parent"] = parent
    return __send_read_msg(mainSocket, dumps({"method": "createImageView", "params": args}))

