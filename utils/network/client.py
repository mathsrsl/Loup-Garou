import socket
import random
from threading import Thread
from datetime import datetime
import time

class Client:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.separator_token = "<SEP>"
        self.s = socket.socket()
        self.message = ["0"]
    def listen_for_messages(self):
        while True:
            message = self.s.recv(1024).decode()
            print("\n" + message)
    def send_message(self):
        # finally, send the message
        while True:
            self.s.send(self.message[0].encode())
        
            time.sleep(1)

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

        t1 = Thread(target=self.send_message)

        t1.daemon = True

        t1.start()


    def send(self, message):
        self.message = [message]

# c = Client("toto", "localhost", 8888)

# c.start()

# while True:
    
#     c.send("toto")

#     time.sleep(1)

#     c.send("tutu")

#     time.sleep(1)