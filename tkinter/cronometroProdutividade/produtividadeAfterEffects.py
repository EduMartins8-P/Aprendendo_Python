import tkinter as tk
import pygetwindow as gw
import time
import threading

class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Artista trabalhando")

        self.tempo = 0          
        self.rodando = True
        self.status_text = "PAUSADO"  

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 40))
        self.label.pack(padx=20, pady=20)

        self.status = tk.Label(root, text=self.status_text, font=("Arial", 20), fg="red")
        self.status.pack()


        self.thread = threading.Thread(target=self.atualizar_tempo, daemon=True)
        self.thread.start()

        self.atualizar_interface()
        self.root.protocol("WM_DELETE_WINDOW", self.fechar)

    def atualizar_tempo(self):
        while self.rodando:
            janela = gw.getActiveWindow()
            if (
                janela
                and "after effects" in janela.title.lower()
                and self.root.title().lower() not in janela.title.lower()
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
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()