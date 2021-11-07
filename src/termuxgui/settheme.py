from json import dumps

from termuxgui.__send_msg import __send_msg

def settheme(mainSocket, aid, statusbarcolor, colorprimary, windowbackground, textcolor, coloraccent):
    '''Sets the Theme fro an Activity.'''
    __send_msg(mainSocket, dumps({"method": "setTheme", "params": {"aid": aid, "statusBarColor": statusbarcolor, "colorPrimary": colorprimary, "windowBackground": windowbackground, "textColor": textcolor, "colorAccent": coloraccent}}))
