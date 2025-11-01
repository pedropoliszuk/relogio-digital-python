from tkinter import *
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

# cores
cor1 = "#292828" # preto
cor2 = "#fafcff" # branco

fundo = cor1
cor = cor2

janela=Tk()
janela.title("Relógio Digital")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=fundo)

def relogio(): 

    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text = hora)
    l1.after(200, relogio)
    l2.config(text = dia_semana + "    " + str(dia) + "/" + str(mes) + "/" + str(ano))

frame_central = Frame(janela, bg=fundo)
frame_central.pack(expand=TRUE)

l1 = Label(janela, text="", font=("digital-7 80"), bg = fundo, fg = cor)
l1.pack()

l2 = Label(janela, text="", font=("digital-7 20"), bg = fundo, fg = cor)
l2.pack(anchor="center")

relogio()
janela.mainloop()