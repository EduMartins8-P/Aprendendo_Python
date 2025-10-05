from tkinter import *

root = Tk()

label1 = Label(root, text="quero cafe",  font=("Comic Sans MS", 48))
label2 = Label(root, text="pq to cansado",  font=("Comic Sans MS", 48))

label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)

root.geometry("500x300")
root.mainloop()