# Bucle For

# Iteracion sobre una secuencia
# Listas
# cadenas
# rangos de numero

"""for variable_iterable in secuencia:
    codigo a ejecutar"""

# Muestren los valores del 1 al 10, de 1 en 1
#Range

for numero in range (1, 11, 1):
    print(numero)

numeros = [1,2,3,4,5,6,7,8,9,10]

for num in numeros:
    print(num)

cadena = "Hola Mundo"

for letra in cadena:
    print(letra)

suma = 0
for i in range (1, 6):
    suma += i
print(f"La suma es  {suma}")

# Bucle While

# Ejecuta mientras que...

"""
variable = ""

while condicion:
    codigo a ejecutar"""

# Muestren los valores del 1 al 10, de 1 en 1
 
numero = 0

while numero < 11:
    print(numero)
    numero += 1


#          0 1 2 3 4 5 6 7 8 9 
numeros = [1,2,3,4,5,6,7,8,9,10]

num =  0
while num < len(numeros):
    print(numeros[num])
    num += 1

cadena = "Hola Mundo"

letra = 0
while letra < len(cadena):
    print(cadena[letra])
    letra = letra + 1

contador = 1
while contador <= 5:
    print(contador)
    contador += 1


contraseña = "Najash"

intento =  ""
while intento != contraseña:
    intento = input("Ingrese su contraseña: ")
print("Acceso Concedido!")