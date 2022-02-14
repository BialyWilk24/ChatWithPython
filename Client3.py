import socket
import time
import threading

disconnect = False
join = False

server_address = socket.gethostbyname(socket.gethostname())
server_port = 9090
client_port = 0

server = (server_address, server_port)# 192.168.56.1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((server_address, client_port))
s.setblocking(False)

def receving(self, sock):
    while not disconnect:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass

print("Enter your nickname. To exit press ctrl + c")
nickname = input("Nickname: ")

receiv_thread = threading.Thread(target=receving, args=('', s))
receiv_thread.start()

while not disconnect:
    if not join:
        s.sendto(("[" + time.strftime("%H:%M:%S", time.localtime()) + "]" + "[" + nickname + "]" + " >>> join chat ").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()

            if message != "":
                s.sendto(("[" + time.strftime("%H:%M:%S", time.localtime()) + "]" + "[" + nickname + "] ::: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + time.strftime("%H:%M:%S", time.localtime()) + "]" + "[" + nickname + "]" + " <<< left chat ").encode("utf-8"), server)
            disconnect = True

receiv_thread.join()
s.close()
