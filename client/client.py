import socket, os, time, sys

def text(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{'='*80}\n{'    '*9}CLIENT\n{'='*80}')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP, SERVER_PORT = input('Enter "IP:PORT": ').split(':')
text(f'Try conect: {SERVER_IP}')

try:
    client_socket.connect((SERVER_IP, int(SERVER_PORT)))
    text('Conection succes.')
    time.sleep(1)
    while True:
        received_data = client_socket.recv(1024)
        message = received_data.decode('utf-8')
        text(f'Message: {message}')
        check=input()
        if check == 'conection.close()':
            break
except ConnectionRefusedError:
    text('Error: conection faild. Check IP or PORT')
finally:
    client_socket.close()