import titulos

"""**Clase 8: Tuplas y Conjuntos en Python**
"""

tupla = (1, 2, 3, 4, 5)

print(tupla[1])

# tupla[1] = 211 esto es un error!
print("--------------------------")
# Desempaquetado de tuplas

a, b, c, d, e = tupla #Asignacion de cada valor de la tupla a una variable

print(a)
print(b)
print(c)
print(d)
print(e)

import separador

print("Desempaquetado en funciones con return")
print(" ")

def coordenadas():
    return(10,20)

x, y = coordenadas()
print(x,y)

import separador
print("Intercambio de valores sin variable temporal")
print(" ")

a, b = 5, 10 # asigne valor a las variables
print( f"a = {a} y b = {b}")
a, b = b, a # Intercambia su valor
print( f"a = {a} y b = {b}")

import separador

print("Desempaquetado parcial con `*` (operador de agrupación)")
print(" ")

valores = (1, 2, 3, 4, 5, 6)
a, *b, c = valores
print(a)
print(b) # Aqui me crea una lista con los valores intermedios
print(c)

import separador
 
print(" Iterar con `enumerate()")
print(" ")
amigos = ["Nana", "Sarah", "Dania"]
for indice, nombre in enumerate(amigos):
    print(f"{indice}: {nombre}")

import separador
print("----------Ejercicio Practico----------")
print(" ")
estudiantes = [("Ana", 95), ("Juan", 85), ("Pedro", 76), ("Maria", 90)]

# 1. Usar enumerate() para imprimir el índice y el nombre de cada estudiante
for i, (nombre, calificacion) in enumerate(estudiantes, start=1):  # Desempaquetamos la tupla
    print(f"{i}: {nombre} - Calificación: {calificacion}")

    if calificacion >= 80:
        print (f"La Calificacion de {nombre} es {calificacion}, por lo tanto esta Aprobado \n")
    else:
        print (f"La Calificacion de {nombre} esta por debajo del promedio, por lo tanto esta Reprobado \n")


import separador
print("Continuamos ---------")

print("Desempaquetado en Diccionarios")

diccionario = {"nombre": "Danny", "Edad": 42}
clave, valor = diccionario.popitem()
print(clave,valor)

import separador

print("*Concatenación de tuplas")
print(" ")

tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = tupla1 + tupla2
print(tupla3)

print(" ")
print("Conversión entre lista y tupla")
print(" ")

lista = [1, 2, 3]
print(f"Esto es una lista: {lista}")
tupla = tuple(lista)
print(f"Esto es una tupla: {tupla}")

print(" ")
print(" Operaciones con Conjuntos")
print(" ")

conjunto = {1, 2, 3, 4, 4, 2}
print(conjunto) # Elimina los duplicados

print("*Principales operaciones con conjuntos")

#Añadir
conjunto.add(5)
print(conjunto)

# Eliminar
conjunto.remove(2) #Elimina el 2
print(conjunto)

print("Operaciones matematicas con conjuntos")

# Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Unión: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersección: {3, 4}
print(A - B)  # Diferencia: {1, 2}
