import socket
import threading
print('starting')
# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))  # Use your IP address and port
server.listen()
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive(server):    
    c = 0
    while True:
        try:
            print('.')       
            client, address = server.accept()
            ip_address = address[0]
            
            #TODO: Why am I getting requests from 10.244.0.1?
            #TODO: I bet there is a better way to do this
            # if ip_address.startswith('10.244.0.1'):
            #     c = c + 1   
            #     print(f'Ignored connection attempt from {ip_address} , {c}')
            #     client.close()
            #     continue
            
            print(f'Connected with {str(address)}')
            
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            nicknames.append(nickname)
            clients.append(client)

            print(f'Nickname of the client is {nickname}')
            broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
            client.send('Connected to the server!'.encode('utf-8'))

            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()

        except Exception as e:
            print(e)
            
print('Server is listening...')
receive(server)
