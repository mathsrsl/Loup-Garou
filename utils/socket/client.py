import socket
import random
from threading import Thread
from datetime import datetime

class Client:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.separator_token = "<SEP>"
        self.s = socket.socket()

    def listen_for_messages(self):
        while True:
            message = self.s.recv(1024).decode()
            print("\n" + message)

    def start(self):
        # initialize TCP socket
        print(f"[*] Connecting to {self.host}:{self.port}...")
        # connect to the server
        self.s.connect((self.host, self.port))
        print("[+] Connected.")

        # make a thread that listens for messages to this client & print them
        t = Thread(target=self.listen_for_messages)
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

        while True:
            # input message we want to send to the server
            to_send =  input()
            # a way to exit the program
            if to_send.lower() == 'q':
                break
            # add the datetime, name & the color of the sender
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"[{date_now}] {self.name}{self.separator_token}{to_send}"
            # finally, send the message
            self.s.send(to_send.encode())

        # close the socket
        self.s.close()

#c = Client("toto", "localhost", 8888)
#
#c.start()
#



