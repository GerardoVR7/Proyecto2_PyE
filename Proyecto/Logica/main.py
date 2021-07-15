import tkinter as tk
from  tkinter import Label, StringVar, ttk
from tkinter.constants import RAISED
from tkinter.ttk import Button
from ProbabilidadEmpirica import empiricalProbability, arrayCreation
from tkinter.constants import END, INSERT, X
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.window()
        self.stage()

    def window(self):
        self.master.title("Proyecto Probabilidad y estadistica")
        self.master.configure(width=1200, height=700)
        self.master.resizable(0,0)
        self.place(relwidth=1, relheight=1)

    def stage(self):

        var = """Probabilidad de la obtencion de cartas en el juego clash royal"""
        """ventanaP.configure(background="black")"""
        self.label= tk.Label(self,text=var, font='Arial 20').pack()
        self.label= tk.Label(self,text='Total de jugadas:', font='Arial 20').place(x=180,y=180)
        self.entrada1= tk.Entry(self, width=20, borderwidth=4, font='Helvetica 16').place(x=380,y=180)

        self.boton2=Button(self,text="empirica")
        self.boton2.place(x=450,y=250)
        self.boton3=Button(self,text=" ver diagrama de arbol ")
        self.boton3.place(x=550,y=250)
        self.ruta = "Proyecto/Archivos/simulacion_1k.csv"
        self.shots = 1000
        print(self.entrada1.get())
        arrayCreation(self.ruta,self.shots)
        empiricalProbability()
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
