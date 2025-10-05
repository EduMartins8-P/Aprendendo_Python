import sys, os
from tkinter import *
from PIL import ImageTk, Image



def caminho_absoluto(relativo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relativo)
    return os.path.join(os.path.abspath("."), relativo)



root = Tk()
root.title("top 10 pokemons shiny")
root.iconbitmap(caminho_absoluto("imagens/pokemonIcones/icon.ico"))
controle = 9



def antes():
    global controle
    if controle == 0:
        fimLista.config(text="fim da lista")
        return
    fimLista.config(text=" ")
    controle -= 1
    posicao.config(image=pokemons[controle])
    ranking.config(text=f"{controle + 1}° posição")
def depois():
    global controle
    if controle == 9:
        fimLista.config(text="fim da lista")
        return
    fimLista.config(text=" ")
    controle += 1
    posicao.config(image=pokemons[controle])
    ranking.config(text=f"{controle + 1}° posição")



caminhos = [
    "imagens/pokemonIcones/megaGengar.jpg",
    "imagens/pokemonIcones/metagross shiny.png",
    "imagens/pokemonIcones/megaGardevoir.jpeg",
    "imagens/pokemonIcones/charizard shiny.png",
    "imagens/pokemonIcones/mawile.png",
    "imagens/pokemonIcones/rapidash.jpeg",
    "imagens/pokemonIcones/chandelure.jpeg",
    "imagens/pokemonIcones/mimikyu.jpg",
    "imagens/pokemonIcones/roselia.png",
    "imagens/pokemonIcones/dratini.png"
]



pokemons = []
for caminho in caminhos:
    img = Image.open(caminho_absoluto(caminho)).resize((500, 500), Image.LANCZOS)
    pokemons.append(ImageTk.PhotoImage(img))



voltar = Button(root, text="<<", command=antes)
avancar = Button(root, text=">>", command=depois)
ranking = Label(root, text=f"{controle + 1}° posição")
posicao = Label(root, image=pokemons[controle])
fimLista = Label(root, text=" ")




fimLista.grid(row=2, column=0, columnspan=3)
posicao.grid(row=0, column=0, columnspan=3)
voltar.grid(row=1, column=0, padx=(10, 0))
ranking.grid(row=1, column=1, padx=(10, 10))
avancar.grid(row=1, column=2, padx=(0, 10))



root.mainloop()