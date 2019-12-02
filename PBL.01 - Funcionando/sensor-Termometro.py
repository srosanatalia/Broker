from socket import *
from threading import Thread
import time
from random import randint
from tkinter import *


def envia_mensagens(socket):
    while True:
        time.sleep(3)
        mensagem = [b'termometro', (str(randint(0,50))).encode('utf-8')]
        for linha in mensagem: #manda linha a linha
            sockObjeto.send(linha) #manda a mensagem
            linha = str(linha.decode("utf-8"))
            if (linha.isdigit()):
                linha = int(linha)
                linha = linha // 1 % 100 #garante dois dígitos
                lblTitulo2 = Label (Top, font=('arial', 10), text = 'Temperatura atual: '+ str(linha)+ 'º', width=20)
                lblTitulo2.grid(row=1, column=0)
            #Depois de mandar uma linha, esperamos uma resposta
        
    print("Envio de mensagens encerrado!")


#dados da conexão do cliente

serverHost = 'localhost' #Coloco o endereõ de IP do servidor
serverPort = 8000

sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
sockObjeto.connect((serverHost, serverPort)) #Conexão
envia = Thread(target=envia_mensagens, args=(sockObjeto,))

root = Tk()
root.geometry('400x100')
root.title('Termômetro')
root.configure(background='white')
Top = Frame(root, width=400, height=50, bd=3, relief='raise')
Top.pack(side=TOP) #posicionamento

lblTitulo = Label (Top, font=('arial', 20), text = 'Termômetro', width=23)
lblTitulo.grid(row=0, column=0)

envia.start()

root.mainloop()


