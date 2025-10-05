from tkinter import *

root = Tk()

def triste():
    ototexto = Label(root, text = "fica tisti nao mo")
    ototexto.grid(row = 2, column = 0)
def feliz():
    ototexto = Label(root, text = "ebaaa uwu")
    ototexto.grid(row = 2, column = 0)

texto = Label(root, text = "ta borocoxozinha?", font = ("", 48))
botao = Button(root, text = "to :(", font = ("",48), command = triste, fg="red")
botao2 = Button(root, text = "to otima :D", font = ("",48), command = feliz)

texto.grid(row = 0, column = 0)
botao.grid(row = 1, column = 1)
botao2.grid(row = 1, column = 0)

root.mainloop()