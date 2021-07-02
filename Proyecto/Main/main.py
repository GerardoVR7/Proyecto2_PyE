import tkinter as tk
from  tkinter import ttk
from tkinter.ttk import Button

ventanaP = tk.Tk()
ventanaP.geometry("400x400")
ventanaP.title("proyecto")
ventanaP.configure(background="black")
boton1=Button(ventanaP,text="probabilidad clasica ")
boton1.place(x=10,y=10)
boton2=Button(ventanaP,text=" empirica y subjetiva ")
boton2.place(x=10,y=40)




ventanaP.mainloop()

