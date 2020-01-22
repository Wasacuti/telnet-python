
import getpass
import sys
import telnetlib

HOST = "localhost"
user = input("Ingrese el usuario: ")
password = getpass.getpass(prompt="Ingrese la clave: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"ping 8.8.8.8 -c 5 \n")
tn.write(b"exit\n")

print(tn.read_all())
