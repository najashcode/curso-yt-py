import titulos 

# Clase 2 Semana 2

# Listas
print("---------------------------------------------")
print("        CLase 2 de la Segunda Semana")
print("---------------------------------------------")

#Sintaxys 
# mi_lista = []

frutas = ["Manzana", "Pera", "Mango"]

mixta = [25, "Python", True, 3.14]

print(frutas)
print(mixta)

# Acceder a la lista

print(frutas[0])

print(frutas[-2])

# Cambiar el valor de las listas
#Agregar elementos
frutas.append("Uvas")

print(frutas)

frutas.insert(1, "Kiwi")
print(frutas)

#Eliminar elementos

print(frutas)
frutas.remove("Uvas")
print(frutas)

ultimo = frutas.pop()
print(ultimo)
print(frutas)

frutas.pop()
print(frutas)

coches = ["Mazda", "Mercedez", "BMW", "Audi"]

print(coches)

"""for carro in coches:
    print(carro)

"""

for i, carro in enumerate(coches):
    print(f"Indice {i}: {carro}")

indice = 0 # Creamos variable inicializada en 0

while indice < len(coches): # Mientras que indice sea menor a longitud de coches
    print(coches[indice]) # Imprime el elemento en la posicion "indice" de la lista "Coches"
    indice += 1 # Incrementa el valor de indice en 1

 #indice = 0 → coches[0] → "Toyota" imprime Toyota
 #indice = 1 → coches[1] → "Mercedez" Imprimre Mercedez
print("----------------------")
for carro in coches:
    print (carro)


# Concatenar listas

lista1 = [1,2,3,4,5]
lista2 = [6, 7, 8, 9]
lista_completa = lista1 + lista2
print(lista_completa)

print("------------------------")
frutas.append("Banana")
print(frutas)

if "Banana" in frutas:
    print("La banana esta en la lista")
else: print("NO Se encontro")

#Ordenas las listas

numeros = [3,7,5,1,4,2,6]
numeros.sort()#Ordena de menor a mayor
print(numeros)

print(len(frutas))

# 1. CREAR UNA LISTA CON LOS NOMBRES DE 5 AMIGOS

amigos = ["Nana", "Sarah", "Dania", "Ian", "Branco"]
print(amigos)

