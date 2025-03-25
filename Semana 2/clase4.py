import titulos

print("-------- Diccionarios en Python --------")

import separador

# Almacenan pares Clave Valor
# se define con llaves {}
# Cada elemento tiene una clave unica que apunta a un valor
# Son modificables, se puede agregar o eliminar elementos

# Sintaxys

nombre_diccionario =  {
    "clave" : "valor",
    "clave2" : "valor2"
}

persona = {
    "nombre" : "Danny",
    "edad" : 42,
    "telefono" : "No tiene" ,
    "ciudad" : "Sevilla"
}

print(persona)

#  Acceder a los valores del Diccionario

print(persona["nombre"]) #Accedo al indice
print(persona.get("edad", "No disponible")) # Uso get para acceder a la clave

# Modificar Diccionarios

persona["edad"] = 31
persona["profesion"] = "Programador"

print(persona)

# Eliminar elementos del diccionario

"""Podemos eliminar elementos usando `del`, `.pop()` o `.popitem()`.  """

del persona["ciudad"] # Esto elimina directamente la clave con su valor
print(persona)

edad = persona.pop("edad") #ELimina edad y la almacena en una variable
print(edad)

ultima = persona.popitem() #Elimina el ultimo elemento agregado
print (persona)

# Lo restauramos con ejercicio

persona["edad"] = 42
persona["profesion"] = "Programador"
persona["Ciudad"] = "Sevilla"
print(persona)

persona["telefono"] = 614357122
print(persona)

# Iterar sobre claves

for clave in persona:
    print(clave, ":", persona[clave]) # Imprime clave con su valor

# Iterar sobre valores

for valor in persona.values():
    print(valor) #Solo imprime el valor

# Iterar sobre claves y valores

for clave, valor in persona.items():
    print(clave, ":", valor)

# Diccionarios anidados

usuarios = {
    "usuario1": {"nombre": "Ana", "edad": 25},
    "usuario2": {"nombre": "Carlos", "edad": 39}
}

print(usuarios["usuario1"]["nombre"])

# Ejercicios

# 1. 

biblio = {
    "titulo" : "Las sombras",
    "autor" : "Danniel Kent",
    "año" : 2025
}

print(biblio)

biblio["paginas"] = 220
print(biblio)

paises = {
    "Colombia" : "Bogota",
    "España" : "Madrid",
    "portugal" : "Lisboa",
    "Argentina" : "Buenos Aires"
}

for pais in paises:
    print(pais, ":", paises[pais])


