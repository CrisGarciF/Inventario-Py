import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Cine")
ventana.configure(width=800,height=800)

salaActual= [0]
etiquetas1 = [[0] * 10 for i in range(7)]
etiquetas2 = [[0] * 10 for i in range(7)]
etiquetas3 = [[0] * 10 for i in range(7)]

estilo = ttk.Style()
estilo.configure("Green.TLabel", background="green", foreground="white", padding=8)
for fila in range(7):
        for columna in range(10):
            texto = str(columna + 1) + '|' + chr(ord('a') + fila)
            etiquetas1[fila][columna] = ttk.Label(ventana, text=texto, style="Green.TLabel")
            etiquetas2[fila][columna] = ttk.Label(ventana, text=texto, style="Green.TLabel")
            etiquetas3[fila][columna] = ttk.Label(ventana, text=texto, style="Green.TLabel")

def cajaCine1():
    for fila in range(7):
        for columna in range(10):
            etiquetas2[fila][columna].place(x=900,y=900)
            etiquetas3[fila][columna].place(x=900,y=900)
            etiquetas1[fila][columna].grid(row=fila, column=columna, padx=10, pady=10)


def cajaCine2():
    for fila in range(7):
        for columna in range(10):
            etiquetas1[fila][columna].place(x=900,y=900)
            etiquetas3[fila][columna].place(x=900,y=900)
            etiquetas2[fila][columna].grid(row=fila, column=columna, padx=10, pady=10)



#funcion para crear la salas del cine
def cajaCine3():
    for fila in range(7):
        for columna in range(10):
            etiquetas1[fila][columna].place(x=900,y=900)
            etiquetas2[fila][columna].place(x=900,y=900)
            etiquetas3[fila][columna].grid(row=fila, column=columna, padx=10, pady=10)

#Funcion para pintar las sillas 

def pintarSilla1():
    silla = entrada.get()
    if salaActual[0] == 1 :
        if '|' in silla:
            columna, fila = silla.split('|')
            if columna.isdigit() and fila.isalpha() and len(fila) == 1:
                columna = int(columna) - 1
                fila = ord(fila.lower()) - ord('a')
                if 0 <= columna < 10 and 0 <= fila < 7:
                    etiquetas1[fila][columna].configure(background='red')
                    print("El puesto",silla, "Esta ocupado")

    elif salaActual[0] == 2:
        if '|' in silla:
            columna, fila = silla.split('|')
            if columna.isdigit() and fila.isalpha() and len(fila) == 1:
                columna = int(columna) - 1
                fila = ord(fila.lower()) - ord('a')
                if 0 <= columna < 10 and 0 <= fila < 7:
                    etiquetas2[fila][columna].configure(background='red')
                    print("El puesto",silla, "Esta ocupado")

    elif salaActual[0] == 3:
        if '|' in silla:
            columna, fila = silla.split('|')
            if columna.isdigit() and fila.isalpha() and len(fila) == 1:
                columna = int(columna) - 1
                fila = ord(fila.lower()) - ord('a')
                if 0 <= columna < 10 and 0 <= fila < 7:
                    etiquetas3[fila][columna].configure(background='red')
                    print("El puesto",silla, "Esta ocupado")


#Funciones para el menu de las salas
def Sala1():
    salaActual[0] = 1
    print("Sala 1")
    cajaCine1()
    pintarSilla1()
    

def Sala2():
    salaActual[0] = 2
    print("Sala 2")
    cajaCine2()
    pintarSilla1()

def Sala3():
    salaActual[0] = 3
    print("Sala 3")
    cajaCine3()
    pintarSilla1()

def selecionSalas():
    menuSalas = tk.Menu(ventana)
    ventana.config(menu=menuSalas)

    Salas = tk.Menu(menuSalas, tearoff=0)
    menuSalas.add_cascade(label="Seleccion de Salas", menu=Salas)

    Salas.add_command(label="Sala 1", command=Sala1)
    Salas.add_command(label="Sala 2", command=Sala2)
    Salas.add_command(label="Sala 3", command=Sala3)
    Salas.add_command(label="Salir", command=ventana.quit)
    
selecionSalas()

#Botones y Texto de entrada


textSilla = ttk.Label(ventana, text="Silla")
textSilla.grid(row=7, column=0, padx=10, pady=10)
entrada = ttk.Entry(ventana)
entrada.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

btnAnadir = ttk.Button(ventana, text="Añadir", command=pintarSilla1)
btnAnadir.grid(row=7, column=0, columnspan=15, padx=10, pady=10)

ventana.mainloop()