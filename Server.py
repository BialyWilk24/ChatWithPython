import socket
import time

ip = socket.gethostbyname(socket.gethostname())
port = 9090

print(ip)
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

disconnect = False
print("[ Server Started ]")

while not disconnect:
    try:
        data, addr = server.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                server.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        disconnect = True

server.close()
