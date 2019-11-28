from socket import *
from threading import Thread


#dados da conexão com o servidor

meuHost = ''
minhaPorta = 8000
#Inscritos
aplicacoes_inscritas = []

def ConversaSimultanea(a,b):
    mensagem = ""
    while True:
        print ("loop")
        mensagem = aplicacoes_inscritas[a].recv(5000)
        if not mensagem:
            break
        aplicacoes_inscritas[b].sendall(mensagem)
    conexao.close()

sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
sockObjeto.bind((meuHost, minhaPorta))
sockObjeto.listen(5) #limita

for i in range(2):
    print ("esperando o "+ str(i+1) +"º cliente conectar-se")
    conexao, endereco = sockObjeto.accept()
    print("O servidor esta conectado por", endereco)
    aplicacoes_inscritas.append(conexao)
    
t1 = Thread(target=ConversaSimultanea, args=(1,0,)).start()
t2 = Thread(target=ConversaSimultanea, args=(0,1,)).start()
