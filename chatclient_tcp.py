#Funcionalidades:
#Ao fazer conexao com o servidor, o cliente registrar no servidor o nome do usuario, a mensagem e o IP

import socket
HOST = socket.gethostbyname('localhost')
PORT = 11000

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect((HOST,PORT))

print('\n')
print ('Cliente Inicializado ...\n')
print ('Para registro de nomes, use: (#registrar) ou (#exit) para sair.' + '\n')
message = input ('Digite um  comando: ')

print('\n')

if message[0] == "#":

    if message == '#exit':
        tcp_client_socket.close
    elif message == "#registrar":
        byte_msg = message.encode('utf-8')
        tcp_client_socket.send(byte_msg)
        #print(tcp_client_socket.send)
elif message[0] != '#':
    print('O COMANDO DIGITADO NÃO FAZ PARTE DESTE PROTOCOLO.','\t''\n' 'TENTE NOVAMENTE ...')


data = tcp_client_socket.recv(1024)

if data[0] == "#":
    if data == "#quem":
        nome =  input ('Qual seu nome?:')
        byte_nome = message.encode('utf-8')
        tcp_client_socket.send(byte_nome)

tcp_client_socket.close

#cond = 'Cliente desconectado do servidor.'
#if data == '#exit':
    #print(tcp_client_socket.cose)

#byte_msg = message.encode('utf-8')
#tcp_client_socket.send(byte_msg)
#data = tcp_client_socket.recv(1024)

#tcp_client_socket.close
