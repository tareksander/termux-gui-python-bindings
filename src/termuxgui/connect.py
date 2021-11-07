from socket import socket, AF_UNIX, SOCK_STREAM, timeout, SOL_SOCKET, SO_PEERCRED
from subprocess import run, DEVNULL
from secrets import choice
from string import ascii_letters, digits
from os import getuid
from struct import unpack

def __check_user(s):
    uid = unpack("III",s.getsockopt(SOL_SOCKET, SO_PEERCRED, 12))[1]
    return uid == getuid()

def connect(printerrormessage=True):
    '''Connects to the Termux:GUI plugin
    
    Returns (mainSocket, eventSocket) if the connection was successful.
    
    In case of an error the plugin is likely not installed, None is returned and an error message is printed, unless the printMessageOnError parameter is set to False.'''
    adrMain = ''.join(choice(ascii_letters+digits) for i in range(50))
    adrEvent = ''.join(choice(ascii_letters+digits) for i in range(50))
    mainss = socket(AF_UNIX, SOCK_STREAM)
    eventss = socket(AF_UNIX, SOCK_STREAM)
    mainss.bind('\0'+adrMain)
    eventss.bind('\0'+adrEvent)
    mainss.listen(1)
    eventss.listen(1)
    mainss.settimeout(5)
    eventss.settimeout(5)
    run(["am","broadcast","-n","com.termux.gui/.GUIReceiver","--es", "mainSocket",adrMain,"--es", "eventSocket",adrEvent],stdout=DEVNULL,stderr=DEVNULL)
    try:
        main = mainss.accept()[0]
        mainss.close()
        event = eventss.accept()[0]
        eventss.close()
        # check for the termux uid to see if it is really the plugin that has connected
        if not __check_user(main) or not __check_user(event):
            main.close()
            event.close()
            return NONE
        main.sendall(b'\x01')
        ret = b''
        while len(ret) == 0:
            ret = ret + main.recv(1)
        if ret[0] != 0:
            main.close()
            event.close()
            return None
        return main, event
    except timeout:
        # Not everything is closed on error, but on error the program should exit anyways, freeing the sockets
        if printerrormessage:
            print("Could not connect to Termux:GUI. Is the plugin installed?")
        return None

