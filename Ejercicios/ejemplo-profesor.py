import tkinter as tk
from tkinter import ttk

class Convertidor(tk.Frame):
    def __init__(self,parent,px,py):
        super().__init__(parent)
        self.TextoGuia=ttk.Label(parent,text="Ingrese metros",font=('Calibri',13))
        self.TextoGuia.place(x=px,y=py)
        self.Entrada=ttk.Entry(parent,font=('Calibri',15))
        self.Entrada.place(x=px,y=py+30,width=100)
        self.Boton=ttk.Button(parent,text="Convertir",command=self.AccionB)
        self.Boton.place(x=px,y=py+60,width=100)
        self.Resultado=ttk.Label(parent)
        self.Resultado.place(x=px,y=py+90)

    def AccionB(self):
        Centimetros=100*float(self.Entrada.get())
        self.Resultado.config(text="Son "+str(Centimetros)+" centimetros")

def Ponercuadritos():
    for i in range(len(Cuadritos)):
        Cuadritos[i].place(x=200,y=i*30,width=20)
def SeleccionLista():
    S=CajaLista.curselection()
    print(ListaNombres[S[0]])
    print(NombreAdentro.get())

    
Ventana=tk.Tk()
Ventana.title("Metros->Centimetros")
Ventana.configure(width=600,height=400)
Conv3=Convertidor(Ventana,0,0)

Cuadritos=[ttk.Label(Ventana,background="red") for i in range(10)]


BotonCuadros=ttk.Button(Ventana,text="SacarCuadros",command=Ponercuadritos)
BotonCuadros.place(x=0,y=300)

CajaLista=tk.Listbox(Ventana,font=('Calibri',18))

CajaLista.place(x=300,y=20)
ListaNombres=['a','b','c','d','e','f','g','h','i']*10
for i,j in enumerate(ListaNombres):
    CajaLista.insert(i,j)
botonSeleccion=ttk.Button(Ventana,text="Seleccion",command=SeleccionLista)
botonSeleccion.place(x=300,y=350)
BarraDesplazamiento=ttk.Scrollbar(Ventana)
BarraDesplazamiento.place(x=550,y=20,height=300)
CajaLista.config(yscrollcommand=BarraDesplazamiento.set)
BarraDesplazamiento.config(command = CajaLista.yview)
NombreAdentro=tk.StringVar(Ventana)
MenuD=ttk.OptionMenu(Ventana,NombreAdentro,"Seleccione","1","2","Colombia")
MenuD.place(x=0,y=200)
Ventana.mainloop()