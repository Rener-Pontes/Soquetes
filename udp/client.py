import socket as skt
import struct

sock: skt.socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

n1, n2 = map(int, input("Digite dois números: ").split())
message: bytes = struct.pack(">ii", n1, n2)

sock.sendto(message, ("", 12000))
data, serverAddr = sock.recvfrom(2048)

sum: int = struct.unpack(">i", data)[0]
print("resultado da soma foi: {}".format(sum))

sock.close()
