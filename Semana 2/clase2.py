import titulos

lista = ["Najash", 31, True, 3,14]

print (lista)

#Indice siempre comienza en 0

print (lista[0])
#Najash

print(lista[-2])
#3

lista[2] = "Code"
print(lista) 

lista.append("Youtube Curso")
print (lista)

lista.insert(1, "Bienvenidos")
print(lista)

lista.remove(31)
print(lista)

lista.pop()
print(lista)

usuario = ["Danny", "39917", 40 ]
print(usuario)

for usuarios in usuario:
    print (usuarios)

for i, usuarios in enumerate(usuario):
    print(f"Indice{i}: {usuarios}")


frutas = ["Manzana", "Pera", "Mango"]

indice = 0

while indice < len(frutas):
    print(frutas[indice])
    indice += 1

lista2 = [2,2,3,4,5,6]
lista3 = [7,9,0]
nuevaLista = lista2 + lista3
print(nuevaLista)

if "Piña" in frutas:
    print ("La manzana Existe!")
else:
    print("El elemento No existe, intente con uno nuevo")

numeros = [3,5,7,8,1,2,4,0.9]
print(numeros)
numeros.sort()
print(numeros)

print(len(frutas))
