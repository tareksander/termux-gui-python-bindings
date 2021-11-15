from socket import socket, AF_UNIX, SOCK_STREAM, timeout, SOL_SOCKET, SO_PEERCRED
from subprocess import run, DEVNULL
from secrets import choice
from string import ascii_letters, digits
from os import getuid
from struct import unpack

from termuxgui.object.event import Event

def _check_user(s):
    uid = unpack("III",s.getsockopt(SOL_SOCKET, SO_PEERCRED, 12))[1]
    return uid == getuid() 


class Connection:
    def __init__(self):
        adrMain = ''.join(choice(ascii_letters+digits) for i in range(50))
        adrEvent = ''.join(choice(ascii_letters+digits) for i in range(50))
        mainss = socket(AF_UNIX, SOCK_STREAM)
        eventss = socket(AF_UNIX, SOCK_STREAM)
        with mainss, eventss:
            mainss.bind('\0'+adrMain)
            eventss.bind('\0'+adrEvent)
            mainss.listen(1)
            eventss.listen(1)
            mainss.settimeout(5)
            eventss.settimeout(5)
            run(["am","broadcast","-n","com.termux.gui/.GUIReceiver","--es", "mainSocket",adrMain,"--es", "eventSocket",adrEvent],stdout=DEVNULL,stderr=DEVNULL)
            try:
                main = mainss.accept()[0]
                try:
                    event = eventss.accept()[0]
                    try:
                        # check for the termux uid to see if it is really the plugin that has connected
                        if not _check_user(main) or not _check_user(event):
                            main.close()
                            event.close()
                            raise RuntimeError("Plugin doesn't have the same UID")
                        main.sendall(b'\x01')
                        ret = b''
                        while len(ret) == 0:
                            ret = ret + main.recv(1)
                        if ret[0] != 0:
                            main.close()
                            event.close()
                            raise RuntimeError("Invalid Protocol version response")
                        self._main = main
                        self._event = event
                    except Exception as e:
                        event.close()
                        raise e
                except Exception as e:
                    main.close()
                    raise e
            except timeout:
                raise RuntimeError("Could not connect to Termux:GUI. Is the plugin installed?")
    
    def events(self):
        yield Event(__read_msg(self._event))
    
    def toast(self, text, long=False):
        __send_msg(self._main, dumps({"method": "toast", "params": {"text": text, "long": long}})) 
    
    def totermux(self):
        '''Returns to the termux task. This is a shorthand for running am start to start the termux activity.'''
        run(["am","start","-n","com.termux/.app.TermuxActivity"],stdout=DEVNULL,stderr=DEVNULL)
    
    def close(self):
        self._main.close()
        self._event.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()
        return False
    
    
    
