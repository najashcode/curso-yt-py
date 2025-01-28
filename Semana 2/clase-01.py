# Bucle For

#for variable in secuencia:
    #Codigo a ejecutar


# Recorrer una lista

numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print(num)
print(" ")
print("Ejercicio 2")
#Recorrer Cadenas

mensaje = "Bienvenido"

for letra in mensaje:
    print(letra)
print(" ")
print("Uso de Range")
# Range

for i in range(0, 11, 2):
    print(i)


print("---------------------------------")

print("Bucle While")

print("---------------------------------")


#sintaxys

"""while condicion :
    Codigo a ejecutar"""

#Contar hasta 5

contador = 1

while contador <= 5:
    print(f"Contador : {contador}")
    contador += 1

print(" ")

print("Entrada de datos. ")


contraseña = "Python"

intentos = ""

while intentos != contraseña:
    intentos = input("Ingrese una Contraseña valida!. ")
print("Acceso Concedido")


"""Ejercicios

### **Ejercicios con `for`**  
1. Imprime los números del 1 al 10.  OK 
2. Calcula la suma de los números en una lista: `[3, 5, 7, 9]`.  
3. Recorre una palabra y muestra cada letra en una nueva línea.  
4. Genera los cuadrados de los números del 1 al 5 y guárdalos en una lista.  
5. Imprime los números pares del 2 al 20 usando `range()`.

"""

# 1.

for i in range(1,11):
    print(i)

"""### **Ejercicios con `while`**  
1. Imprime los números del 1 al 10 usando un bucle `while`.  OK
2. Crea un contador que se detenga al llegar a 100, sumando de 10 en 10.  
3. Pide al usuario ingresar números y termina cuando ingrese un número negativo.  
4. Genera una tabla de multiplicar del 3 utilizando un bucle `while`.  
5. Usa un bucle `while` para contar cuántas veces se lanza un dado hasta obtener un 6 (usa números aleatorios).  
"""

# 1.

numeros = 11

num = 1

while num != numeros:
    print(num)
    num +=1

