#Uso del If

if (True):
    print("Algo")

edad = int(input("Digite su Edad: "))

if edad >= 18:
    print("El usuario es mayor de edad.")
else: print("El usuario es menor de edad.") 

# Verificar las notas del estudiante

"""90 = excelente
80 = muy Bueno
70 = bueno
60 = regular
-50 = malo"""

nota = int(input("Ingrese la nota: "))

if nota >= 90:
    print("Su calificacion es Excelente.")
elif nota >= 80:
    print("Su calificacion es Muy Buena.")
elif nota >=70:
    print("Su calificacion es Buena")
elif nota >= 60:
    print("Ha aprobado con la minima")
else: print("Reprobado!")


#1. Escribe un programa que solicite un número y diga si es negativo, cero o positivo.

numero = int(input("Digite un numero: "))

if numero < 0:
    print("El numero es Negativo")
elif numero >= 0:
    print("El numero es Positivo")
else: print("El numero es Cero")

#2. Crea un programa que pida una contraseña y verifique si es correcta.

contrasena = input("Digite la contraseña: ")

if contrasena == "Danny":
    print("La contraseña es correcta!")
else: print("La contraseña es incorrecta, por favor intente de nuevo!")

#3. Programa un sistema que solicite la edad del usuario y determine si puede votar.

edad = int(input("Por favor Digite su edad: "))

if edad >= 18:
    print("Usuario mayor, puede votar!")
else: print("No apto para votar")

#4. Haz un juego que compare un número secreto con un número ingresado por el usuario.

secreto = 198

user = int(input("Ingrese un numero: "))

if user == secreto:
    print("Numero Acertado")
else: print("Intentelo nuevamente")


"""
El if es una estructura condicional que permite validad si una
condicion es verdadera o falsa.

el ELIF es una estructura if dentro de otra y permite validar 
varias opciones

la estructura ELSE permite cerrar un IF ya que valida la opcion
contraria al if

"""
