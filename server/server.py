import socket, os, time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_local_id():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_addres = s.getsockname()[0]
        s.close()
        return ip_addres
    except:
        return 'Ip not found'

server_socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socet.listen(1)
print(f'Server ip: {get_local_id()}')
print('Started. Wait conecting...')
client_socket, client_addres = server_socet.accept()
clear()
print(f'Client conected: {client_addres}')

while True:
    message = input('Enter your message: ')
    client_socket.send(message.encode('utf-8'))
    clear()
    print(f'Sended: {message}')
    if message == 'conection.close()':
        break

client_socket.close()
server_socet.close()
clear()
print('Server off.')