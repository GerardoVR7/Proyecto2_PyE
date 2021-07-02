import tkinter as tk
from  tkinter import Label, StringVar, ttk
from tkinter.constants import RAISED
from tkinter.ttk import Button

ventanaP = tk.Tk()
ventanaP.geometry("400x400")
ventanaP.title("proyecto")
var = StringVar()
"""ventanaP.configure(background="black")"""
label=Label(ventanaP,textvariable=var , relief=RAISED)
var.set("Probabilidad de obtencion de cartas en el juego Clash Royal")
label.pack()
boton1=Button(ventanaP,text="probabilidad clasica ")
boton1.place(x=150,y=60)
boton2=Button(ventanaP,text=" empirica y subjetiva ")
boton2.place(x=150,y=100)
boton3=Button(ventanaP,text=" ver diagrama de arbol ")
boton3.place(x=150,y=140)




ventanaP.mainloop()

