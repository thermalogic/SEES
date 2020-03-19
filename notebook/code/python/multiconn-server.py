import selectors
sel = selectors.DefaultSelector()

# ...
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))

lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
