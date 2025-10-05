from tkinter import *

root = Tk()
root.title("eita como calcula")
reserva = None


def soma(numero):
    global reserva
    if numero == "+":
        reserva = entrada.get()
        entrada.delete(0, END)

    elif numero == "=":
        resultado = int(reserva) + int(entrada.get())
        entrada.delete(0, END)
        entrada.insert(0, resultado)
    
    else:
        entrada.insert(END, numero)

    


entrada = Entry(root, width = 10, bg = "light gray", fg = "red", borderwidth = 10)

botao0 = Button(root, text = "0", padx = 40, pady= 30, command = lambda: soma(0))
botao1 = Button(root, text = "1", padx = 40, pady= 30, command = lambda: soma(1))
botao2 = Button(root, text = "2", padx = 40, pady= 30, command = lambda: soma(2))
botao3 = Button(root, text = "3", padx = 40, pady= 30, command = lambda: soma(3))
botao4 = Button(root, text = "4", padx = 40, pady= 30, command = lambda: soma(4))
botao5 = Button(root, text = "5", padx = 40, pady= 30, command = lambda: soma(5))
botao6 = Button(root, text = "6", padx = 40, pady= 30, command = lambda: soma(6))
botao7 = Button(root, text = "7", padx = 40, pady= 30, command = lambda: soma(7))
botao8 = Button(root, text = "8", padx = 40, pady= 30, command = lambda: soma(8))
botao9 = Button(root, text = "9", padx = 40, pady= 30, command = lambda: soma(9))
botaoIgual = Button(root, text = "=", padx = 40, pady= 30, command = lambda: soma("="))
botaoMais = Button(root, text = "+", padx = 40, pady= 30, command = lambda: soma("+"))
botaoApagar = Button(root, text = "apagar", padx = 25, pady= 30, command = lambda: entrada.delete(0,END))


entrada.grid(row = 0, column = 0)
botao0.grid(row = 4, column = 0)
botao1.grid(row = 1, column = 0)
botao2.grid(row = 1, column = 1)
botao3.grid(row = 1, column = 2)
botao4.grid(row = 2, column = 0)
botao5.grid(row = 2, column = 1)
botao6.grid(row = 2, column = 2)
botao7.grid(row = 3, column = 0)
botao8.grid(row = 3, column = 1)
botao9.grid(row = 3, column = 2)
botaoIgual.grid(row = 4, column = 1)
botaoMais.grid(row = 4, column = 2)
botaoApagar.grid(row = 5, column = 0)


root.mainloop()