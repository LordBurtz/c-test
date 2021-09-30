#this will be the serve

import socket as s

SEPARATOR = "<sep>"
IP = localhost
PORT = 11067

socket = s.socket()
s.bind((IP, PORT))
s.listen(5)

while True:
    c, addr = s.accept(
