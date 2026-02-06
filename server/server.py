import socket, os, time, sys

def text(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{'='*80}\n{'    '*10}CLIENT\n{'='*80}')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
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
server_socet.bind(('0.0.0.0', 12345))
server_socet.listen(1)
print(f'Server ip: {get_local_id()}')
print('Started. Wait conecting...')
client_socket, client_addres = server_socet.accept()
text(f'Client conected: {client_addres}')
time.sleep(1)

while True:
    message = input('Enter your message: ')
    client_socket.send(message.encode('utf-8'))
    text(f'Sended: {message}')
    if message == 'conection.close()':
        break

client_socket.close()
server_socet.close()
text('Server off.')