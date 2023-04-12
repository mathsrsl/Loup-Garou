import socket
from threading import Thread

def listen_for_client(cs, client_sockets, separator_token):
   """
   This function keep listening for a message from `cs` socket
   Whenever a message is received, broadcast it to all other connected clients
   """
   while True:
        try:
           # keep listening for a message from `cs` socket
           msg = cs.recv(1024).decode()
           msg = msg.replace(separator_token, ": ")
        except Exception as e:
           # client no longer connected
           # remove it from the set
           print(f"[!] Error: {e}")
           client_sockets.remove(cs)
       
           # if we received a message, replace the <SEP> 
           # token with ": " for nice printing
           
        # iterate over all connected sockets
        for client_socket in client_sockets:
           # and send the message
           client_socket.send(msg.encode())
        if not msg is None: 
            print(f'message: {msg}\n')

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.separator_token = '<SEP>'

        self.client_sockets = []

        self.s = socket.socket()

    def start(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.s.bind((self.host, self.port))

        self.s.listen(5)

        print(f"[*] Listening as {self.host}:{self.port}")

        while True:
            # we keep listening for new connections all the time
            client_socket, client_address = self.s.accept()
            print(f"[+] {client_address} connected.")
            # add the new connected client to connected sockets
            self.client_sockets.append(client_socket)
            # start a new thread that listens for each client's messages
            t = Thread(target=listen_for_client, args=(client_socket, self.client_sockets, self.separator_token))
            # make the thread daemon so it ends whenever the main thread ends
            t.daemon = True
            # start the thread
            t.start()
        
        # close client sockets
        for cs in client_sockets:
            cs.close()
        # close server socket
        self.s.close()

s = Server('localhost', 8888)

s.start()

