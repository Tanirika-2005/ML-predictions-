from tkinter import *
import tkinter as tk
import os
from PIL import ImageTk
from tkinter import Tk, Text

top=tk.Tk()
top.geometry("900x563")

def helloCallBack():
    os.system('python gui1.py')
    top.destroy()
canvas = Canvas(top, width=900, height=563)
canvas.pack()


image =PhotoImage(file="my.png")
canvas.create_image(0, 0, image=image, anchor=NW)

canvas_id = canvas.create_text(440, 200, anchor="center")
canvas.itemconfig(canvas_id, text="Welcome to BTC predicitons \n using ML algorithm")
canvas.itemconfig(canvas_id, font=("courier",30),fill = 'red')
canvas.insert(canvas_id, 12,"")
B=tk.Button(top,text="start predicting",command= helloCallBack,fg = 'red',bg='black')
B.pack()
B.place(relx=0.5, rely=0.5, anchor=CENTER)
top.mainloop()
