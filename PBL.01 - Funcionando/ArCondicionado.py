from socket import *
from threading import Thread
import time
from tkinter import *

def recebe_mensagens(socket):
    while True:
        data = socket.recv(1024)
        if not data:
            break
        data = str(data.decode("utf-8"))
        if (data.isdigit()):
            data = int(data)
            data = data // 1 % 100 #garante dois dígitos
            if (data > 20):
                lblTitulo2 = Label (Top, font=('arial', 10), text = 'Ligado', width=20)
                lblTitulo2.grid(row=1, column=0)
            else:
                lblTitulo2 = Label (Top, font=('arial', 10), text = 'Desligado', width=20)
                lblTitulo2.grid(row=1, column=0)
    print("Conexão com o servidor encerrada")


def envia_mensagens(socket):
    while True:
        time.sleep(3)
        msg = 'arcondicionado'
        socket.send(msg.encode("utf-8"))
        
    print("Envio de mensagens encerrado!")



#def main():
    #dados da conexão do cliente
serverHost = 'localhost' #Coloco o endereõ de IP do servidor
serverPort = 8000


sockObjeto = socket (AF_INET, SOCK_STREAM) #Usando servidor TCP-IP
sockObjeto.connect((serverHost, serverPort)) #Conexão
envia = Thread(target=envia_mensagens, args=(sockObjeto,))
recebe = Thread(target=recebe_mensagens, args=(sockObjeto,))

root = Tk()
root.geometry('400x100')
root.title('Ar-Condicionado')
root.configure(background='white')
Top = Frame(root, width=400, height=100, bd=3, relief='raise')
Top.pack(side=TOP) #posicionamento

lblTitulo = Label (Top, font=('arial', 20), text = 'Ar-Condicionado', width=23)
lblTitulo.grid(row=0, column=0)

envia.start()
recebe.start()

root.mainloop()
    
    

#if __name__ == "__main__":
#    main()
