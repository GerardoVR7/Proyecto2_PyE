import tkinter as tk
from  tkinter import Label, StringVar, ttk
from tkinter.constants import RAISED
from tkinter.ttk import Button
#from Logica.ProbabilidadEmpirica import arrayCreation, empiricalProbability

ventanaP = tk.Tk()
ventanaP.geometry("1200x700")
ventanaP.title("proyecto")
var = """Probabilidad de la obtencion de cartas en el juego clash royal"""
"""ventanaP.configure(background="black")"""
label= tk.Label(ventanaP,text=var, font='Arial 20').pack()
label= tk.Label(ventanaP,text='Total de jugadas:', font='Arial 20').place(x=180,y=180)
entrada1= tk.Entry(ventanaP).place(x=400,y=190)
boton2=Button(ventanaP,text="empirica")
boton2.place(x=450,y=250)
boton3=Button(ventanaP,text=" ver diagrama de arbol ")
boton3.place(x=550,y=250)




ventanaP.mainloop()

