import socket
import time


# Получаем адрес нашей машины и определяем порт
# Порт выбираем в диапазоне от 1025 до 65000
ip = socket.gethostbyname(socket.gethostname())
port = 9090

print(ip)
clients = []


# Создаём соединение сервeра на IPv4 и UDP и привязываем его к нашему адресу и порту
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

disconnect = False
print("[ Server Started ]")


# Логика работы сервера, пока есть подключение
while not disconnect:
    try:
        data, addr = server.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        time_mess = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + time_mess + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                server.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        disconnect = True

server.close()
