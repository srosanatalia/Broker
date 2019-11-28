from socket import *
from threading import Thread

def recebe_mensagens(socket):
    while True:
        data = socket.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))
    print("Conexão com o servidor encerrada")


def envia_mensagens(socket):
    while True:
        msg = 'Termometro'
        socket.sendall(msg.encode("utf-8"))
        break
    print("Envio de mensagens encerrado!")


#dados da conexão do cliente

serverHost = 'localhost' #Coloco o endereõ de IP do servidor
serverPort = 8000
tipoSensor = b'Termometro'
mensagem = [tipoSensor, b'36'] #b formato de bytes #vai variar

sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
sockObjeto.connect((serverHost, serverPort)) #Conexão
envia = Thread(target=envia_mensagens, args=(sockObjeto,))
recebe = Thread(target=recebe_mensagens, args=(sockObjeto,))

envia.start()
recebe.start()

