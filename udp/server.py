import socket as skt
import struct


serverPort: int = 12000
sock: skt.socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
sock.bind(("", serverPort))

print("Server started ^-^")

while True:
    data, clientAddr = sock.recvfrom(2048)

    n1, n2 = struct.unpack(">ff", data)
    data = struct.pack(">f", n1+n2)
    sock.sendto(data, clientAddr)
