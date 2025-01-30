# Listas
#Sintaxys
mi_lista = []

frutas = ["Manzana", "Pera", "Mango"]

mixta = ["manzana", 25, True, 3.14]

print(frutas, mixta)

print(frutas[0])
print(mixta[3])

print(frutas[-3])

#lo que significa que de atas hacia adelante comienza en 1

frutas[2] = "Banano"
print(frutas)

frutas.append("Mango")#agrega al final
frutas.insert(1, "Mora")#inserta en el indice
print(frutas)

frutas.remove("Mango" )#Elimina por valor
ultimo = frutas.pop()
print (frutas)

print("elemento eliminado: ", ultimo)

frutas.append ("Maracuya")
frutas.append("Fresas")
for i, fruta in enumerate(frutas):
    print(f"Indice {i}: {fruta}")

indice = 0
while indice  < len(frutas):
    print(frutas[indice])
    indice += 1

    