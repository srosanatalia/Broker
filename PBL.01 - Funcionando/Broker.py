from socket import *
from threading import Thread


#dados da conexão com o servidor

meuHost = ''
minhaPorta = 8000
#Inscritos
aplicacoes_inscritas = []
publisher = []
subscribe = []

def Comunicacao():
    mensagem = ""
    while True:
        for i in range (len(aplicacoes_inscritas)): #manda linha a linha
            mensagem = aplicacoes_inscritas[i].recv(5000)
            
            if (mensagem == b'termometro'):
                publisher.append(aplicacoes_inscritas[i])
                mensagem = aplicacoes_inscritas[i].recv(5000)
                print (mensagem)
                for j in range (len(subscribe)):
                    subscribe[j].sendall(mensagem)
                    
            elif ((mensagem == b'arcondicionado')or(mensagem == b'aquecedor')):
                subscribe.append(aplicacoes_inscritas[i])
            
            if not mensagem:
                break
            
    conexao.close()

sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
sockObjeto.bind((meuHost, minhaPorta))
sockObjeto.listen(5) #limita

for i in range(3):
    print ("esperando o "+ str(i+1) +"º cliente conectar-se")
    conexao, endereco = sockObjeto.accept()
    print("O servidor esta conectado por", endereco)
    aplicacoes_inscritas.append(conexao)

t1 = Thread(target=Comunicacao, args=()).start()
t2 = Thread(target=Comunicacao, args=()).start()
t3 = Thread(target=Comunicacao, args=()).start()
