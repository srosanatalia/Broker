from socket import *
import threading


#dados da conexão com o servidor

meuHost = ''
minhaPorta = 8000
#Inscritos
aplicacoes_inscritas = {}

sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
sockObjeto.bind((meuHost, minhaPorta))
sockObjeto.listen(5) #limita

#Testando conexão com o servidor

def conectado(conexao, endereco):
    print("O servidor esta conectado por", endereco)
    print(conexao)
    while True: #Enquanto houverem dados
        data = conexao.recv(1024) #limitei a 1024 bytes de conexão
        if not data:
            break #Se não existirem dados, ele sai
        aplicacoes_inscritas[conexao] = data
        print(data)
        conexao.send(data) #Se houverem dados, ele vai me mostrar
    #print(aplicacoes_inscritas.values())
        for key in aplicacoes_inscritas:
            if (aplicacoes_inscritas[key] == b'Aplicacao'):
                #time.sleep(5)
                key.send(b'a')
                
    conexao.close()

while True:
    conexao, endereco = sockObjeto.accept()
    threading.Thread(target = conectado, args = [conexao, endereco]).start()

