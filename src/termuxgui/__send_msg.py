
def __send_msg(c, msg):
    m = bytes(msg, "utf-8")
    c.sendall((len(m)).to_bytes(4,"big"))
    c.sendall(m)
