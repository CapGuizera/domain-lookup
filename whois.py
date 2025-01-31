#!/usr/share/python

import socket,sys

if len(sys.argv) < 2:
    print("Uso: %s <dominio>" % sys.argv[0])
    sys.exit(1)

else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send((sys.argv[1] + "\r\n").encode())
    resp = s.recv(1024).split()
    whois = resp[19].decode()

    if resp[0].decode() == "No" and resp[1].decode() == "match":
        print("Nenhum resultado encontrado")
    else:
        print("RESPONSÁVEL: %s" % whois)
        print(whois + "\n")
    s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois, 43))
s1.send((sys.argv[1] + "\r\n").encode())
resp1 = s1.recv(1024)
print(resp1.decode())  # Decode the byte response to a string before printing
