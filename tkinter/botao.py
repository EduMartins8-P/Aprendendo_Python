from tkinter import *

root = Tk()

def clicou():
    ototexto = Label(root, text = "n pode ta tarde")
    ototexto.grid(row = 2, column = 0)

texto = Label(root, text = "quer cafe?", font = ("", 48))
botao = Button(root, text = "quero :(", font = ("",48), command = clicou, fg="red")
botao2 = Button(root, text = "num quero :P", font = ("",48), state = DISABLED)

texto.grid(row = 0, column = 0)
botao.grid(row = 1, column = 1)
botao2.grid(row = 1, column = 0)

root.mainloop()