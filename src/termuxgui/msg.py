from json import loads
import array
import socket

def read_msg(s):
    b = b''
    togo = 4
    while togo > 0:
        read = s.recv(togo)
        b = b + read
        togo = togo - len(read)
    togo = int.from_bytes(b, "big")
    b = b''
    while togo > 0:
        read = s.recv(togo)
        b = b + read
        togo = togo - len(read)
    return loads(b.decode("utf-8"))

def send_msg(c, msg):
    m = bytes(msg, "utf-8")
    c.sendall((len(m)).to_bytes(4,"big"))
    c.sendall(m)

def send_read_msg(s, msg):
    send_msg(s, msg)
    return read_msg(s)



def read_msg_fd(s):
    b = b''
    togo = 4
    while togo > 0:
        read = s.recv(togo)
        b = b + read
        togo = togo - len(read)
    togo = int.from_bytes(b, "big")
    b = b''
    fds = array.array("i")
    while togo > 0:
        read, ancdata, _, _ = s.recvmsg(togo, socket.CMSG_LEN(fds.itemsize))
        for cmsg_level, cmsg_type, cmsg_data in ancdata:
            if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
                fds.frombytes(cmsg_data[:len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])
        b = b + read
        togo = togo - len(read)
    if len(fds) != 0:
        return (loads(b.decode("utf-8")), fds[0])
    else:
        return (loads(b.decode("utf-8")),)


