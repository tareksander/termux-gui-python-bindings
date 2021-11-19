from socket import socket, AF_UNIX, SOCK_STREAM, timeout, SOL_SOCKET, SO_PEERCRED
from subprocess import run, DEVNULL
from secrets import choice
from string import ascii_letters, digits
from os import getuid
from struct import unpack
from json import dumps
from select import select


from termuxgui.event import Event
from termuxgui import msg as tgmsg

def _check_user(s):
    uid = unpack("III",s.getsockopt(SOL_SOCKET, SO_PEERCRED, 12))[1]
    return uid == getuid() 


class Connection:
    """This represents a connection to the Termux:GUI plugin and contains all functions that don't act on any particular View, Activity or Task."""
    def __init__(self):
        """When a connection can't be established, a RuntimeError is raised."""
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
        """Waits for events. Use this with "for in" to iterate over incoming events and block while waiting."""
        while True:
            yield Event(tgmsg.read_msg(self._event))
    
    def checkevent(self):
        """If there is at least one event to be read, returns it. If there is no event, returns null. You can use this to e.g. check for events between drawing a frame instead of having to use a separate thread and blocking it."""
        r, _, _ = select([self._event], [], [], 0)
        if len(r) != 0:
            return Event(tgmsg.read_msg(self._event))
        
    
    def toast(self, text, long=False):
        """Sends a Toast. Set long to True if you want to display the text for longer."""
        self.send_msg({"method": "toast", "params": {"text": text, "long": long}}) 
    
    def totermux(self):
        '''Returns to the termux task. This is a shorthand for running "am start" to start the termux activity.'''
        run(["am","start","-n","com.termux/.app.TermuxActivity"],stdout=DEVNULL,stderr=DEVNULL)
    
    def close(self):
        """Closes the connection.
        
        The connection is automatically closed when the program exits, but it's good practice to close the connection yourself when you don't need it anymore or use a "with" statement."""
        self._main.close()
        self._event.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()
        return False
    
    
    def send_msg(self, msg):
        """Send a message to the main socket. You should only need to call this yourself if you want to use methods not yet implemented in the library."""
        if type(msg) is dict:
            msg = dumps(msg)
        tgmsg.send_msg(self._main, msg)
    
    def read_msg(self):
        """Read a message from the main socket. You should only need to call this yourself if you want to use methods not yet implemented in the library."""
        return tgmsg.read_msg(self._main)
    
    def send_read_msg(self, msg):
        """Send a message to the main socket and read a message afterwards. You should only need to call this yourself if you want to use methods not yet implemented in the library."""
        self.send_msg(msg)
        return self.read_msg()
    
    
    
