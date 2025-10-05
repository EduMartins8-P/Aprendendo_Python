from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()


valorCampeao = -1
valorLane = -1
radioCampeao = IntVar(value=-1)
radioLane = IntVar(value=-1)


quadro1 = LabelFrame(root, text = "escolha o campeao", padx = 10, pady = 10)
quadro2 = LabelFrame(root, text = "escolha a lane", padx = 10, pady = 10)
resultado = Label(root, text = " ")


def setarCampeao(valor):
    global valorCampeao
    valorCampeao = valor


def verificar(valor):
    global resultado
    if valor == valorCampeao:
        messagebox.showinfo("lolzero", "CERTINHO :D") 
        root.quit()
    else:
        erro = messagebox.askyesno("burro", "erroukkkkkkk \ntentar de novo?")
        if not erro:
            root.quit()


Radiobutton(quadro1, text = "GWEN", variable = radioCampeao, value = 0, command = lambda: setarCampeao(0)).grid(row = 1, column = 0)
Radiobutton(quadro1, text = "KATARINA", variable = radioCampeao, value = 1, command = lambda: setarCampeao(1)).grid(row = 1, column = 1)
Radiobutton(quadro1, text = "ASHE", variable = radioCampeao, value = 2, command = lambda: setarCampeao(2)).grid(row = 1, column = 2)
Radiobutton(quadro1, text = "SORAKA", variable = radioCampeao, value = 3, command = lambda: setarCampeao(3)).grid(row = 3, column = 0)
Radiobutton(quadro1, text = "RENGAR", variable = radioCampeao, value = 4, command = lambda: setarCampeao(4)).grid(row = 3, column = 1)
Radiobutton(quadro1, text = "KAYLE", variable = radioCampeao, value = 5, command = lambda: setarCampeao(5)).grid(row = 3, column = 2)
Radiobutton(quadro2, text = "TOP", variable = radioLane, value = 0, command = lambda: verificar(0)).grid(row = 1, column = 0)
Radiobutton(quadro2, text = "MID", variable = radioLane, value = 1, command = lambda: verificar(1)).grid(row = 1, column = 1)
Radiobutton(quadro2, text = "BOT", variable = radioLane, value = 2, command = lambda: verificar(2)).grid(row = 1, column = 2)
Radiobutton(quadro2, text = "JUNGLE", variable = radioLane, value = 3, command = lambda: verificar(3)).grid(row = 3, column = 0)
Radiobutton(quadro2, text = "SUP", variable = radioLane, value = 4, command = lambda: verificar(4)).grid(row = 3, column = 1)
Radiobutton(quadro2, text = "KAYLE", variable = radioLane, value = 5, command = lambda: verificar(5)).grid(row = 3, column = 2)



imagemGwen = ImageTk.PhotoImage(Image.open("imagens/campeoes/gwen.png").resize((200, 200)))
imagemKatarina = ImageTk.PhotoImage(Image.open("imagens/campeoes/katarina.jpg").resize((200, 200)))
imagemAshe = ImageTk.PhotoImage(Image.open("imagens/campeoes/ashe.jpeg").resize((200, 200)))
imagemSoraka = ImageTk.PhotoImage(Image.open("imagens/campeoes/soraka.jpg").resize((200, 200)))
imagemRengar = ImageTk.PhotoImage(Image.open("imagens/campeoes/rengar.jpg").resize((200, 200)))
imagemKayle = ImageTk.PhotoImage(Image.open("imagens/campeoes/kayle.jpg").resize((200, 200)))
imagemTop = ImageTk.PhotoImage(Image.open("imagens/campeoes/topLane.jpg").resize((200, 200)))
imagemMid = ImageTk.PhotoImage(Image.open("imagens/campeoes/midLane.jpg").resize((200, 200)))
imagemBot = ImageTk.PhotoImage(Image.open("imagens/campeoes/botLane.jpg").resize((200, 200)))
imagemJungle = ImageTk.PhotoImage(Image.open("imagens/campeoes/jungle.jpg").resize((200, 200)))
imagemSup = ImageTk.PhotoImage(Image.open("imagens/campeoes/sup.jpg").resize((200, 200)))


gwen = Label(quadro1, image = imagemGwen, compound = "top", padx = 20, pady = 20,).grid(row = 0, column = 0)
katarina = Label(quadro1, image = imagemKatarina, padx = 20, pady = 20, compound = "top").grid(row = 0, column = 1)
ashe = Label(quadro1, image = imagemAshe, padx = 20, pady = 20, compound = "top").grid(row = 0, column = 2)
soraka = Label(quadro1, image = imagemSoraka, padx = 20, pady = 20, compound = "top").grid(row = 2, column = 0)
rengar = Label(quadro1, image = imagemRengar, padx = 20, pady = 20, compound = "top").grid(row = 2, column = 1)
kayle = Label(quadro1, image = imagemKayle, padx = 20, pady = 20, compound = "top").grid(row = 2, column = 2)
topLane = Label(quadro2, image = imagemTop, padx = 20, pady = 20, compound = "top").grid(row = 0, column = 0)
midLane = Label(quadro2, image = imagemMid, padx = 20, pady = 20, compound = "top").grid(row = 0, column = 1)
botLane = Label(quadro2, image = imagemBot, padx = 20, pady = 20, compound = "top").grid(row = 0, column = 2)
jungle = Label(quadro2, image = imagemJungle, padx = 20, pady = 20, compound = "top").grid(row = 2, column = 0)
sup = Label(quadro2, image = imagemSup, padx = 20, pady = 20, compound = "top").grid(row = 2, column = 1)
kayleLane = Label(quadro2, image = imagemKayle, padx = 20, pady = 20, compound = "top").grid(row = 2, column = 2)


quadro1.grid(row = 0, column = 0)
quadro2.grid(row = 0, column = 1)
resultado.grid(row = 1, column = 0)


root.mainloop()