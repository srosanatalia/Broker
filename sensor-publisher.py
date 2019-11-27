from socket import *
import threading

class Sensor(threading.Thread): #classe que gera os clientes

    #Threads são linhas de execução concorrentes em um mesmo processo.
    #Elas são concorrentes no sentido de que executam simultaneamente,
    #mas cada um com a sua própria linha de execução - quase como se
    #fossem programas diferentes.
    
    def __init__(self, tipoSensor, server, port, *mensagem):
        self.tipoSensor = tipoSensor #identificacao
        self.server = server #servidor
        self.port = port #porta
        self.msgs = mensagem #mensagem

        threading.Thread.__init__(self)

    def run (self):
        #Cria objeto socket e conecta ao servidor
        sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
        sockObjeto.connect((self.server, self.port)) #Conexão
        ms =input('digite valor')
        ms = ms.encode('utf-8')
        self.msgs = [tipoSensor, ms]
        for linha in self.msgs: #manda linha a linha
            sockObjeto.send(linha) #manda a mensagem
            #Depois de mandar uma linha, esperamos uma resposta
            data = sockObjeto.recv(1024) #Resposta do broker
            print(data)
            print('Sensor ',self.tipoSensor,'mandou', linha)
            #if (self.c == 2):
            #     print('Cliente é o ',self.c,'recebeu', data)
        sockObjeto.close()

#dados da conexão do cliente

serverHost = 'localhost' #Coloco o endereõ de IP do servidor
serverPort = 8000
tipoSensor = b'Termometro'
mensagem = [tipoSensor, b'36'] #b formato de bytes #vai variar
Sensor(tipoSensor, serverHost, serverPort, *mensagem).start()
#for c in range (20):
    #Cliente(c, serverHost, serverPort, *mensagem).start()
#print('Geramos todos os clientes!')


'''
#Cria objeto socket e conecta ao servidor
sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP

sockObjeto.connect((serverHost, serverPorta)) #Conexão

for linha in mensagem: #manda linha a linha
    sockObjeto.send(linha)
    #Resposta do servidor
    data = sockObjeto.recv(1024)
    print('Cliente recebeu:', data)

sockObjeto.close()


#Testando conexão com o servidor

while True:
    conexao, endereco = sockObjeto.accept()
    print("O servidor esta conectado por", endereco)
    while True: #Enquanto houverem dados
        data = conexao.recv(1024) #limitei a 1024 bytes de conexão
        if not data:
            break #Se não existirem dados, ele sai
        conexao.send(b'Eco=>' + data) #Se houverem dados, ele vai me mostrar'''
        
