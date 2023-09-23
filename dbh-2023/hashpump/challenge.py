#!/usr/bin/env python3

import hashlib
import socket
import secrets
import subprocess
import traceback

SAMPLE = b"whoami\n# Just an example"
SECRET = secrets.token_bytes(100)


def sample():
    return SAMPLE.hex(), hashlib.sha512(SECRET + SAMPLE).hexdigest()


def check_signature(dt, h):
    dt = bytes.fromhex(dt.decode())
    print(hashlib.sha512(SECRET + dt).hexdigest(), h.decode())

    if hashlib.sha512(SECRET + dt).hexdigest() == h.decode():
        return True


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('0.0.0.0', 10000)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    stream = connection.makefile('wrb')
    try:
        while True:
            connection.sendall(f"""Führe jeglichen Code aus den du dir ausdenken kannst ohne eigene Rechenleistung zu nutzen!
            
Dieser Service ist exclusiv für VIP-Nutzer. Bitte denke daran deinen Code mit deinem Schlüssel zu signieren.
            
Beispiel: {':'.join(sample())}
            
> """.encode("utf-8"))
            data = stream.readline().strip()
            if data:
                dt, h = data.split(b":")
                if check_signature(dt, h):
                    commands = bytes.fromhex(dt.decode()).split(b'\n')
                    for command in commands:
                        try:
                            connection.sendall(subprocess.check_output(command, shell=True))
                        except:
                            pass
            else:
                break
    except:
        traceback.print_exc()
    finally:
        connection.close()
