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
        self.ruta = "Proyecto/Archivos/simulacion_1k.csv"
        self.shots =  100000
        arrayCreation(self.ruta, self.shots)
        var = """Probabilidad de la obtencion de cartas en el juego clash royal"""
        """ventanaP.configure(background="black")"""
        self.label= tk.Label(self,text=var, font='Arial 20').pack()
        self.btn2 = tk.Button(self, text='Calcular 10k', command=self.generatethings)
        self.btn2.place(x=30, y=80)
        self.btn3 = tk.Button(self, text='Calcular 50k', command=self.generatethings2)
        self.btn3.place(x=110, y=80)
        self.btn4 = tk.Button(self, text='Calcular 100k', command=self.generatethings3)
        self.btn4.place(x=190, y=80)
        self.boton2=Button(self,text="empirica")
        self.boton2.place(x=450,y=250)
        self.boton3=Button(self,text=" ver diagrama de arbol ")
        self.boton3.place(x=550,y=250)
    
    def generatethings(self):
        self.intento = 10000
        plataProbability=empiricalProbability(self.intento)
        print("AQUI SE DECIDE TODO: ",plataProbability)
        self.label= tk.Label(self,text=plataProbability, font='Arial 20').place(x=180,y=380)

    def generatethings2(self):
        self.intento = 50000
        plataProbability,oroProbability,giganteProbability,magicoProbability,superMagicoProbability,superEspecialProbability,legendarioProbability,s1Probability,s2Probability,s3Probability,s4Probability,s5Probability,s6Probability,s7Probability,s8Probability,s9Probability,s10Probability,s11Probability,s12Probability =empiricalProbability(self.intento)


    def generatethings3(self):
        self.intento = 100000
        plataProbability,oroProbability,giganteProbability,magicoProbability,superMagicoProbability,superEspecialProbability,legendarioProbability,s1Probability,s2Probability,s3Probability,s4Probability,s5Probability,s6Probability,s7Probability,s8Probability,s9Probability,s10Probability,s11Probability,s12Probability =empiricalProbability(self.intento)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
