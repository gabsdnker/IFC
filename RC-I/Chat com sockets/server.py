#Author: Gabrielli Danker
#Date: 26/06/2024
#Servidor para o chat com sockets

#Obs:. Rodar python server.py primeiro

import socket
import threading

# Configurações do servidor
HOST = '0.0.0.0'  # Endereço IP do servidor
PORT = 12345      # Porta do servidor

# Lista de clientes conectados
clients = []
nicknames = []
client_connections = {}  # Dicionário para armazenar conexões de clientes por apelido

# Função para retransmitir mensagens para todos os clientes conectados
def broadcast(message, sender_nickname=None):
    for client in clients:
        try:
            client.send((message + '\n').encode('utf-8'))
        except:
            # Remover cliente da lista se a conexão falhar
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            del client_connections[nickname]
            client.close()
            broadcast(f'{nickname} foi desconectado.', nickname)

# Função para enviar lista de clientes conectados
def send_client_list(client):
    client_list = '\n'.join(nicknames)
    client.send(f'Clientes conectados:\n{client_list}\n'.encode('utf-8'))

# Função para lidar com cada cliente individualmente
def handle_client(client):
    while True:
        try:
            # Recebe mensagem do cliente
            message = client.recv(1024).decode('utf-8')
            if message:
                if message.lower() == 'exit':
                    index = clients.index(client)
                    nickname = nicknames[index]
                    clients.remove(client)
                    nicknames.remove(nickname)
                    del client_connections[nickname]
                    client.close()
                    broadcast(f'{nickname} saiu do chat.', nickname)
                    break
                elif message.startswith('/list'):
                    send_client_list(client)
                elif message.startswith('/private'):
                    parts = message.split(' ', 2)
                    if len(parts) >= 3:
                        recipient_nickname = parts[1]
                        if recipient_nickname in client_connections:
                            client_connections[recipient_nickname].send(f'Mensagem privada de {nicknames[clients.index(client)]}: {parts[2]}'.encode('utf-8'))
                        else:
                            client.send(f'Cliente {recipient_nickname} não encontrado.\n'.encode('utf-8'))
                    else:
                        client.send('Formato de mensagem privada inválido. Use /private <apelido> <mensagem>\n'.encode('utf-8'))
                else:
                    broadcast(message, nicknames[clients.index(client)])
        except Exception as e:
            # Remover cliente em caso de erro
            print(f'Erro ao lidar com cliente: {str(e)}')
            if client in clients:
                index = clients.index(client)
                nickname = nicknames[index]
                clients.remove(client)
                nicknames.remove(nickname)
                del client_connections[nickname]
                client.close()
                broadcast(f'{nickname} foi desconectado devido a um erro.', nickname)
            break

# Função principal do servidor
def receive():
    server.listen()
    print('Servidor ouvindo...')
    while True:
        # Aceita conexão de um cliente
        client, address = server.accept()
        print(f'Conectado com {str(address)}')

        # Solicita e armazena apelido do cliente
        client.send(' '.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        client_connections[nickname] = client  # Armazena a conexão do cliente pelo apelido

        # Exibe e retransmite informações sobre o novo cliente
        print(f'Apelido do cliente é {nickname}')
        broadcast(f'{nickname} entrou no chat.', nickname)
        client.send('Conectado ao servidor!\n'.encode('utf-8'))

        # Inicia thread para lidar com o cliente
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Inicializa o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
receive()
