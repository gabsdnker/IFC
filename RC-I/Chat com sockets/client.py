#Author: Gabrielli Danker
#Date: 26/06/2024
#Cliente para o chat com sockets

#Obs:. Rodar python client.py em várias janelas do terminal para quantos clientes quiser
#Lista de conectados "/list"
#Conversa privada "/private <apelido> <mensagem>"
#Sair do chat "exit"

import socket
import threading

# Configurações do cliente
HOST = 'localhost'  # Endereço IP do servidor (substitua pelo IP do servidor)
PORT = 12345        # Porta do servidor

# Solicita o apelido do usuário
nickname = input("Escolha seu apelido: ")

# Inicializa o cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Envia o apelido para o servidor
client.send(nickname.encode('utf-8'))

# Flag para indicar desconexão voluntária
disconnected = False

# Função para receber mensagens do servidor
def receive():
    global disconnected
    while True:
        try:
            # Recebe mensagem do servidor
            message = client.recv(1024).decode('utf-8').strip()
            print(message)
        except:
            # Fecha conexão em caso de erro
            if not disconnected:
                print("Ocorreu um erro!")
            client.close()
            break

# Função para enviar mensagens ao servidor
def write():
    global disconnected
    while True:
        message = input()
        if message.lower() == 'exit':
            disconnected = True
            client.send(f'{nickname} saiu do chat.'.encode('utf-8'))
            client.close()
            break
        elif message.startswith('/list'):
            client.send('/list'.encode('utf-8'))
        elif message.startswith('/private'):
            parts = message.split(' ', 2)
            if len(parts) >= 3:
                recipient_nickname = parts[1]
                client.send(f'/private {recipient_nickname} {parts[2]}'.encode('utf-8'))
            else:
                print('Formato de mensagem privada inválido. Use /private <apelido> <mensagem>')
        else:
            client.send(f'{nickname}: {message}'.encode('utf-8'))

# Inicia threads para enviar e receber mensagens
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
