# Ejercicio 1
t = [i for i in range(999 + 1)]
print(t)


#Ejercicio 2
t = [i / 1000 for i in range(1000)]
print(t)


#Ejercicio 3
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = [i for i in X if i % 3 == 0]
print(b)


#Ejercicio 4
p = "Hola mundo"
v = [i for i in p]
print(v)


#Ejercicio 5
X = ["Odio", "Choclitos", "Infarto", "Vertigo", "Salon”,“Gato", "Uña"]
m = [i for i in X[::-1]]
print(m)


#Ejercicio 6
Cedulas = {1062343998: "Carlos Piedrahita", 1052333768: "Jaime Ruiz", 1045212351: "Esteban Ochoa"}

lis = [[nombre, cedula] for cedula, nombre in Cedulas.items()]
print(lis)


#Ejercicio 7
Datos = [
  "Antioquia_Minería_1993", "Córdoba_Químicos_2003", "Cauca_Agropecuaria_2001",
  "Valle del Cauca_Alimenticia_2001"
]
res = [dato.split("_") for dato in Datos]
print(res)


#Ejercicio 8
x = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
result = [sublista[0] * sublista[1] for sublista in x]
print(result)


#Ejercicio 9
Notas = [[3, 1.2, 3.4, 5, 4.3], [4.2, 2.8, 3.4, 3.2, 4.3],
         [3.6, 2, 3, 3.1, 1.4]]

Nombres1 = ["Daniel", "Esteban", "Juan", "Andres", "Kevin"]
Nombres2 = ["Julian", "David", "Kelly", "Camila", "John"]
Nombres3 = ["Carlos", "Vanesa", "Manuel", "Jose", "Pablo"]
Nombres = [Nombres1, Nombres2, Nombres3]

reprobados = [
  nombre for list, nombres_estu in zip(Notas, Nombres)
  for nombre, nota in zip(nombres_estu, list) if nota < 3
]
print(reprobados)


#Ejercicio 10
Notas = [[3, 1.2, 3.4, 5, 4.3], [4.2, 2.8, 3.4, 3.2, 4.3],
         [3.6, 2, 3, 3.1, 1.4]]
Nombres1 = ["Daniel", "Esteban", "Juan", "Andres", "Kevin"]
Nombres2 = ["Julian", "David", "Kelly", "Camila", "John"]
Nombres3 = ["Carlos", "Vanesa", "Manuel", "Jose", "Pablo"]
Nombres = [Nombres1, Nombres2, Nombres3]

lista = [[nombre, "Salón " + str(i + 1), nota]
         for i, sublist in enumerate(Notas)
         for nombre, nota in zip(Nombres[i], sublist)]
print(lista)