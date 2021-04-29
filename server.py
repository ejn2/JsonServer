from socket import *
from os import path

#####################################################
#        Servidor python para arquivos json         #
#####################################################

IP = '127.0.0.1'
PORT = 3003

data = open(path.join('./data.json')).read() #Faz a leitura do arquivo selecionado.

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen(7)

print(f"|Running...\n|=> http://{IP}:{PORT}\n") #Informa quando o servidor está "rodando"

while True:
    cli, addr = server.accept()
    
    req = cli.recv(1024) #Contêm dados das requisições

    cli.send(b"HTTP/1.1 200 ok\r\n")
    cli.send(b"Content-Type: application/json\r\n\r\n") #Enviar header informando o tipo de conteúdo.
    cli.send(data.encode())
    cli.close()
