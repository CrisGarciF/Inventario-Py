import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox

class Reservacine(tk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.numerosala = []
        self.guardarsilla = tk.Entry(ventana)
        self.guardarsilla.grid(row=7, column=1, padx=6, pady=6)

        self.aniadirbtn = tk.Button(ventana, text="Añadir silla", command=self.aniadirsilla)
        self.aniadirbtn.grid(row=7, column=2, padx=5, pady=5)

        self.menu = tk.Menu(ventana)
        ventana.config(menu=self.menu)
        self.menu_opciones = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Opciones", menu=self.menu_opciones)
        self.menu_opciones.add_command(label="sala 1", command=self.salas1)
        self.menu_opciones.add_command(label="sala 2", command=self.salas2)
        self.menu_opciones.add_command(label="sala 3" , command=self.salas3)

    
        for i in range(7):
            fila = []
            for j in range(10):
                puestos = tk.Label(ventana, text=f"{j+1}|{chr(i+97)}", background="green")
                puestos.grid(row=i, column=j+1, padx=5, pady=5)
                fila.append(puestos)
            self.numerosala.append(fila)

    def aniadirsilla(self):
        ind = self.guardarsilla.get()
        fila, columna = self.filacolumna(ind)

        if self.numerosala[columna][fila].cget("background") == "green":
            self.numerosala[columna][fila].config(bg="red")
        else: 
            MessageBox.showwarning("Aviso", "Silla ocupada")

    def filacolumna(self, indicador):
        filaletra, columnas = indicador.split("|")
        fila = int(filaletra) - 1
        columna = ord(columnas) - ord("a")
        return fila, columna
    
    def salas1():
        print("sala 1")
    def salas2():
        print("sala 2")
    def salas3():
        print("sala 3")

ventana = tk.Tk()
ventana.title("Sillas disponibles")
reservacine = Reservacine(ventana)
reservacine.grid(row=10, column=8, padx=5, pady=5)

ventana.mainloop()