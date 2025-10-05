import tkinter as tk
import pygetwindow as gw
import time
import threading
from pynput import mouse

class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Artista trabalhando")

        self.tempo = 0          
        self.rodando = True
        self.status_text = "PAUSADO"  
        self.botao_pressionado = False
        self.movendo = False
        self.ultimo_pos = None

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 40))
        self.label.pack(padx=20, pady=20)

        self.status = tk.Label(root, text=self.status_text, font=("Arial", 20), fg="red")
        self.status.pack()

        self.listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        self.listener.start()

        self.thread = threading.Thread(target=self.atualizar_tempo, daemon=True)
        self.thread.start()

        self.atualizar_interface()
        self.root.protocol("WM_DELETE_WINDOW", self.fechar)

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            self.botao_pressionado = pressed
            if pressed:
                self.ultimo_pos = (x, y)

    def on_move(self, x, y):
        if self.botao_pressionado:
            if self.ultimo_pos is None:
                self.ultimo_pos = (x, y)
            elif (x, y) != self.ultimo_pos:
                self.movendo = True
                self.ultimo_pos = (x, y)

    def atualizar_tempo(self):
        while self.rodando:
            janela = gw.getActiveWindow()
            if (
                janela
                and "krita" in janela.title.lower()
                and self.root.title().lower() not in janela.title.lower()
                and self.botao_pressionado
                and self.movendo
            ):
                self.tempo += 0.05  
                self.status_text = "CONTANDO"
            else:
                self.status_text = "PAUSADO"
                self.movendo = False 
            time.sleep(0.05)

    def atualizar_interface(self):
        horas = int(self.tempo) // 3600
        minutos = (int(self.tempo) % 3600) // 60
        segundos = int(self.tempo) % 60
        self.label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        self.status.config(
            text=self.status_text, 
            fg="green" if self.status_text == "CONTANDO" else "red"
        )
        self.root.after(50, self.atualizar_interface) 

    def fechar(self):
        self.rodando = False
        self.listener.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()