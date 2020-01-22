import getpass
import sys
import telnetlib

HOST = "192.168.0.1"
user = input("Ingrese el usuario: ")
password = getpass.getpass(prompt="Ingrese la clave: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"clave\n")
tn.write(b"conf t\n")
tn.write(b"hostname Router1 \n")
tn.write(b"int lo0 \n")
tn.write(b"ip add 192.168.10.1 255.255.255.0 \n")
tn.write(b"exit\n")
tn.write(b"do wr\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all())
