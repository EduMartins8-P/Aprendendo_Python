from tkinter import *
from PIL import ImageTk, Image
import os
import sys



root = Tk()
root.title("vasco")
root.iconbitmap("C:/Users/eduar/Downloads/cruz_de_malta.ico")



def encerrar():
    msg = Label(root, text="pobrema teu", font=("Comic Sans MS", 20))
    msg.grid(row = 2)
    root.after(1000, root.quit)

def ebavasco():
    msg = Label(root, text="lindo maravilhoso te amo", font=("Comic Sans MS", 20))
    msg.grid(row = 2)
    root.after(1000, root.quit)    

def caminhoAbsoluto(relativo):
    try:
        base = sys._MEIPASS
    
    except AttributeError:
        base = os.path.abspath(".")
    
    return os.path.join(base, relativo)



imgOriginal = Image.open(caminhoAbsoluto("imagens/codigoIcones/flamengo.png"))
imgRedimensionada = imgOriginal.resize((100,100), Image.LANCZOS)
imgBotao = ImageTk.PhotoImage(imgRedimensionada)
imgOriginal2 = Image.open(caminhoAbsoluto("imagens/codigoIcones/botafogo.png"))
imgRedimensionada2 = imgOriginal2.resize((100,100), Image.LANCZOS)
imgBotao2 = ImageTk.PhotoImage(imgRedimensionada2)
imgOriginal3 = Image.open(caminhoAbsoluto("imagens/codigoIcones/fluminense.png"))
imgRedimensionada3 = imgOriginal3.resize((100,100), Image.LANCZOS)
imgBotao3 = ImageTk.PhotoImage(imgRedimensionada3)
imgOriginal4 = Image.open(caminhoAbsoluto("imagens/codigoIcones/vasco.png"))
imgRedimensionada4 = imgOriginal4.resize((100,100), Image.LANCZOS)
imgBotao4 = ImageTk.PhotoImage(imgRedimensionada4)



fechar = Button(root, image = imgBotao, text = "aqui eh flamengo", compound = "bottom", command = encerrar, borderwidth = 0)
fechar2 = Button(root, image = imgBotao2, text = "aqui eh botafogo", compound = "bottom", command = encerrar, borderwidth = 0)
fechar3 = Button(root, image = imgBotao3, text = "aqui eh fluminense", compound = "bottom", command = encerrar, borderwidth = 0)
fechar4 = Button(root, image = imgBotao4, text = "aqui eh vasco", compound = "bottom", command = ebavasco, borderwidth = 0)



fechar.grid(row = 0, column = 0)
fechar2.grid(row = 0, column = 1)
fechar3.grid(row = 1, column = 0)
fechar4.grid(row = 1, column = 1)



root.mainloop()