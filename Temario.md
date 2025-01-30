# Curso de pyton 
En esta guia encontrara el material del curso
* [Introduccion a Python](#clase1)
* [Variables y Tipos de Datos](#clase2)
* [Operadores Matemáticos y Lógicos](#clase3)
* [Función Input y Print](#clase4)
* [Condicionales (if, else, elif)](#clase5)
* [Semana 2](#semana2)
* [ Bucles `for` y `while](#clase6)



# Clase1

 **Clase 1: Introducción a Python y Configuración del Entorno**

### **1. Instalación de Python**

1. **Descargar e instalar Python:**

   - Ve a la página oficial [python.org](https://www.python.org/).
   - Descarga la versión más reciente.
   - Durante la instalación, marca la opción "Add Python to PATH".
   - Completa la instalación.

2. **Verificar la instalación:**

   - Abre la terminal (cmd en Windows, Terminal en Mac/Linux).
   - Escribe `python --version` o `python3 --version` y presiona Enter. Debe mostrar la versión instalada.

### **2. Usar un entorno como VSCode o Jupyter Notebooks**

1. **Visual Studio Code:**

   - Descarga e instala [VSCode](https://code.visualstudio.com/).
   - Abre VSCode y busca la extensión "Python" en la sección de extensiones.
   - Instala la extensión y reinicia VSCode.

2. **Jupyter Notebooks:**

   - Abre la terminal y escribe: `pip install notebook` para instalarlo.
   - Ejecuta `jupyter notebook` para abrir el entorno.

### **3. Primer programa: "Hola, Mundo"**

1. Abre VSCode o Jupyter Notebook.
2. Crea un archivo llamado `hola_mundo.py`.
3. Escribe el siguiente código:
   ```python
   print("Hola, Mundo")
   ```
4. Guarda el archivo y ejecúta el programa.

### **4. Conceptos básicos de sintaxis**

1. **Comentarios:**

   - Un comentario se escribe usando el símbolo `#`.

   ```python
   # Esto es un comentario
   print("Aprendiendo Python")
   ```

2. **Variables:**

   - Se crean asignando valores a nombres.

   ```python
   nombre = "Danny"
   edad = 25
   print(nombre, edad)
   ```

3. **Tipos de datos:**

   - Números enteros: `int`
   - Números decimales: `float`
   - Cadenas de texto: `str`
   - Booleanos: `bool`

4. **Entrada y salida:**

   ```python
   nombre = input("¿Cómo te llamas? ")
   print("Hola,", nombre)
   ```

5. **Indentación:**

   - Python usa espacios para definir bloques de código.

   ```python
   if True:
       print("Esto está indentado correctamente")
   ```
[Volver al inicio](#top)


# clase2

# **Clase 2: Variables y Tipos de Datos**

### **1. Tipos de Datos en Python**

Python maneja varios tipos de datos básicos:

1. **Enteros (int):**
   - Números sin decimales.
   - Ejemplo:
     ```python
     edad = 25
     temperatura = -10
     print(type(edad))  # <class 'int'>
     ```

2. **Flotantes (float):**
   - Números con decimales.
   - Ejemplo:
     ```python
     precio = 19.99
     promedio = -3.14
     print(type(precio))  # <class 'float'>
     ```

3. **Cadenas de texto (str):**
   - Texto encerrado entre comillas simples o dobles.
   - Ejemplo:
     ```python
     nombre = "Danny"
     saludo = 'Hola, mundo'
     print(type(nombre))  # <class 'str'>
     ```

4. **Booleanos (bool):**
   - Representan valores de verdadero o falso.
   - Ejemplo:
     ```python
     es_estudiante = True
     esta_lloviendo = False
     print(type(es_estudiante))  # <class 'bool'>
     ```

---

### **2. Asignación de Variables**

1. **Sintaxis básica:**
   - Se utiliza el signo `=` para asignar valores a variables.
   - Ejemplo:
     ```python
     nombre = "Danny"
     edad = 30
     esta_aprendiendo = True
     ```

2. **Asignación múltiple:**
   - Se pueden asignar varios valores en una sola línea.
   - Ejemplo:
     ```python
     x, y, z = 5, 10, 15
     print(x, y, z)
     ```

3. **Reasignación de variables:**
   - Las variables pueden cambiar su valor en cualquier momento.
   - Ejemplo:
     ```python
     mensaje = "Hola"
     print(mensaje)
     mensaje = "Adios"
     print(mensaje)
     ```

4. **Nombres de variables:**
   - Deben comenzar con una letra o guion bajo (`_`).
   - No pueden contener espacios ni caracteres especiales.
   - Ejemplos válidos: `edad`, `_nombre`, `usuario_1`.
   - Ejemplos inválidos: `1usuario`, `nombre-usuario`.

---

### **3. Conversiones de Tipos**

1. **Conversión explícita:**
   - Uso de funciones como `int()`, `float()`, `str()`, `bool()`.
   - Ejemplos:
     ```python
     # De cadena a entero
     numero = int("42")
     print(numero, type(numero))

     # De entero a cadena
     texto = str(123)
     print(texto, type(texto))

     # De cadena a flotante
     decimal = float("3.14")
     print(decimal, type(decimal))

     # De entero a booleano
     valor = bool(1)  # Cualquier número distinto de cero es True
     print(valor, type(valor))
     ```

2. **Errores comunes:**
   - Intentar convertir cadenas no numéricas a enteros o flotantes genera errores.
   - Ejemplo:
     ```python
     # Esto generará un error
     numero_invalido = int("Hola")  # ValueError
     ```
[Volver al inicio](#top)

# Clase3
# **Clase 3: Operadores Matemáticos y Lógicos**

### **1. Operadores Matemáticos**

Python permite realizar operaciones matemáticas básicas usando los siguientes operadores:

1. **Suma (`+`)**
   ```python
   resultado = 5 + 3
   print("Suma:", resultado)  # 8
   ```

2. **Resta (`-`)**
   ```python
   resultado = 10 - 4
   print("Resta:", resultado)  # 6
   ```

3. **Multiplicación (`*`)**
   ```python
   resultado = 7 * 2
   print("Multiplicación:", resultado)  # 14
   ```

4. **División (`/`)**
   ```python
   resultado = 15 / 3
   print("División:", resultado)  # 5.0
   ```

5. **División Entera (`//`)**
   ```python
   resultado = 17 // 3
   print("División Entera:", resultado)  # 5
   ```

6. **Módulo o Resto (`%`)**
   ```python
   resultado = 17 % 3
   print("Resto:", resultado)  # 2
   ```

7. **Exponenciación (`**`)**
   ```python
   resultado = 2 ** 3
   print("Exponenciación:", resultado)  # 8
   ```

---

### **2. Operadores Lógicos**

Estos operadores permiten combinar condiciones lógicas:

1. **`and` (y):** Devuelve `True` si ambas condiciones son verdaderas.
   ```python
   a = True
   b = False
   print(a and b)  # False
   ```

2. **`or` (o):** Devuelve `True` si al menos una de las condiciones es verdadera.
   ```python
   a = True
   b = False
   print(a or b)  # True
   ```

3. **`not` (no):** Invierte el valor lógico.
   ```python
   a = True
   print(not a)  # False
   ```

---

### **3. Operadores de Comparación**

Se utilizan para comparar valores:

1. **Igual a (`==`)**
   ```python
   print(5 == 5)  # True
   print(5 == 3)  # False
   ```

2. **Distinto de (`!=`)**
   ```python
   print(5 != 3)  # True
   ```

3. **Mayor que (`>`)**
   ```python
   print(7 > 3)  # True
   ```

4. **Menor que (`<`)**
   ```python
   print(2 < 5)  # True
   ```

5. **Mayor o igual que (`>=`)**
   ```python
   print(4 >= 4)  # True
   ```

6. **Menor o igual que (`<=`)**
   ```python
   print(3 <= 4)  # True
   ```
[Volver al inicio](#top)

---------------------------------

# Clase4
# **Clase 4: Función `input()` y `print()` con Formateo de Cadenas**

### **1. Función `input()` para recibir datos**

La función `input()` permite al usuario ingresar datos desde el teclado. Devuelve siempre una cadena de texto.

#### **Sintaxis:**
```python
variable = input("Mensaje para el usuario: ")
```

#### **Ejemplo 1:** Solicitar el nombre del usuario
```python
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)
```

#### **Ejemplo 2:** Ingresar dos números y sumarlos
```python
num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")
suma = int(num1) + int(num2)
print("La suma es:", suma)
```
*Nota:* Convertimos los valores a enteros usando `int()`.

---

### **2. Función `print()` y Formateo de Cadenas**

La función `print()` muestra información en la consola.

#### **Sintaxis básica:**
```python
print(valor1, valor2, ..., sep=" ", end="\n")
```

- **`sep=" "`**: Define el separador entre valores (por defecto, un espacio).
- **`end="\n"`**: Define lo que sucede al final de la salida (por defecto, nueva línea).

#### **Ejemplo 1:** Mostrar un mensaje simple
```python
print("Hola, Mundo")
```

#### **Ejemplo 2:** Mostrar múltiples valores separados por un guion
```python
print("Python", "es", "genial", sep="-")
```

#### **Ejemplo 3:** Mostrar una línea sin salto de línea
```python
print("Esto es una línea", end=" ")
print("y esto sigue en la misma línea.")
```

---

### **3. Formateo de Cadenas con `f-strings`**

Los `f-strings` permiten incluir variables dentro de cadenas de texto de manera sencilla y legible.

#### **Sintaxis:**
```python
print(f"Texto {variable} más texto")
```

#### **Ejemplo 1:** Mostrar un mensaje personalizado
```python
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
print(f"Hola {nombre}, tienes {edad} años.")
```

#### **Ejemplo 2:** Realizar cálculos directamente en el `f-string`
```python
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
print(f"La suma de {num1} y {num2} es {num1 + num2}")
```
[Volver al inicio](#top)

--------------------------------------

# Clase5
**Clase 5: Condicionales (if, else, elif)**

### **1. Estructura Condicional**
Las estructuras condicionales permiten ejecutar diferentes bloques de código según una condición.

#### **Sintaxis básica:**
```python
if condicion:
    # Bloque de código si la condición es verdadera
elif otra_condicion:
    # Bloque de código si la segunda condición es verdadera
else:
    # Bloque de código si ninguna condición es verdadera
```

---

### **2. Uso de `if`**
Ejecuta un bloque de código si la condición es verdadera.

#### **Ejemplo 1:** Verificar si un número es positivo
```python
numero = int(input("Ingresa un número: "))
if numero > 0:
    print(f"{numero} es un número positivo.")
```

---

### **3. Uso de `if-else`**
Define un bloque de código para cuando la condición es falsa.

#### **Ejemplo 2:** Comprobar si un número es par o impar
```python
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
```

---

### **4. Uso de `if-elif-else`**
Permite evaluar múltiples condiciones en orden.

#### **Ejemplo 3:** Clasificar una nota de examen
```python
nota = int(input("Ingresa tu nota: "))
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")
```

---

### **5. Ejercicios Sencillos para Practicar**

1. Escribe un programa que solicite un número y diga si es negativo, cero o positivo.
2. Crea un programa que pida una contraseña y verifique si es correcta.
3. Programa un sistema que solicite la edad del usuario y determine si puede votar.
4. Haz un juego que compare un número secreto con un número ingresado por el usuario.

[Volver al inicio](#top)

--------------------------------------


# Semana2
# Clase1

# **Clase 6: Bucles `for` y `while`**

Los bucles permiten repetir bloques de código varias veces según una condición, es decir, el buicle se repite hasta que se terminan los elementos de esa coleccion.
---

### **1. Bucle `for`**

El bucle `for` itera sobre una secuencia (como una lista, cadena o rango de números).

#### **Sintaxis:**
```python
for variable in secuencia:
    # Código a ejecutar
```

#### **Ejemplo 1:** Recorrer una lista
```python
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)
```

#### **Ejemplo 2:** Recorrer una cadena
```python
mensaje = "Hola"
for letra in mensaje:
    print(letra)
```

#### **Ejemplo 3:** Usar `range()`
```python
for i in range(5):
    print(f"Número: {i}")
```

---

### **2. Bucle `while`**

El bucle `while` ejecuta el bloque de código mientras una condición sea verdadera.

#### **Sintaxis:**
```python
while condicion:
    # Código a ejecutar
```

#### **Ejemplo 4:** Contar hasta 5
```python
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
```

#### **Ejemplo 5:** Entrada de datos con `while`
```python
contraseña = "python"
intento = ""
while intento != contraseña:
    intento = input("Introduce la contraseña: ")
print("¡Acceso concedido!")
```

---

### **3. Uso de Contadores y Acumuladores**

- **Contador:** Variable que se incrementa de manera controlada.
- **Acumulador:** Variable que acumula valores.

#### **Ejemplo 6:** Sumar los primeros 5 números
```python
suma = 0
for i in range(1, 6):
    suma += i
print(f"La suma es {suma}")
```

#### **Ejemplo 7:** Contar números pares
```python
pares = 0
for i in range(1, 11):
    if i % 2 == 0:
        pares += 1
print(f"Hay {pares} números pares entre 1 y 10")
```

---

### **Consejos:**
- Evita bucles infinitos verificando condiciones correctamente.
- Usa `break` para salir de un bucle y `continue` para pasar a la siguiente iteración.

[Volver al inicio](#top)

----------------------------------

# Clase7

# **Día 2: Listas en Python**

Las listas son estructuras de datos fundamentales en Python que permiten almacenar colecciones de elementos de manera ordenada y modificable.

---

## **1. Creación de Listas**

En Python, una lista se define utilizando corchetes `[]`, y sus elementos se separan por comas:

```python
# Lista vacía
mi_lista = []

# Lista con elementos
frutas = ["manzana", "banana", "cereza"]

# Lista con diferentes tipos de datos
mixta = [25, "Python", True, 3.14]

print(frutas)
print(mixta)
```

---

## **2. Acceso a Elementos de una Lista**

Cada elemento de una lista tiene un índice que empieza desde `0`.

```python
frutas = ["manzana", "banana", "cereza"]

print(frutas[0])  # Acceder al primer elemento
print(frutas[1])  # Acceder al segundo elemento
print(frutas[-1]) # Acceder al último elemento
```

> **Nota:** Los índices negativos permiten acceder desde el final hacia el inicio.

---

## **3. Modificación de Listas**

Puedes cambiar el valor de un elemento accediendo a su índice:

```python
frutas = ["manzana", "banana", "cereza"]
frutas[1] = "pera"  # Modificar "banana" por "pera"
print(frutas)
```

También puedes agregar o eliminar elementos:

```python
# Agregar elementos
frutas.append("naranja")  # Agrega al final
frutas.insert(1, "kiwi")  # Inserta en el índice 1

# Eliminar elementos
frutas.remove("pera")  # Elimina por valor
ultimo = frutas.pop()  # Elimina el último y lo retorna

print(frutas)
print("Elemento eliminado:", ultimo)
```

---

## **4. Iterar sobre Listas con Bucles**

Puedes recorrer una lista con un bucle `for`:

```python
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
```

Si necesitas acceder también a los índices, usa `enumerate()`:

```python
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")
```

Para recorrer una lista con `while`:

```python
indice = 0
while indice < len(frutas):
    print(frutas[indice])
    indice += 1
```

---

## **5. Otras Operaciones con Listas**

### **Concatenación de listas**
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_completa = lista1 + lista2
print(lista_completa)
```

### **Comprobación de existencia**
```python
if "banana" in frutas:
    print("La banana está en la lista.")
```

### **Ordenar listas**
```python
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()  # Ordena la lista de menor a mayor
print(numeros)
```

### **Obtener la longitud de una lista**
```python
print(len(frutas))print
```

---

## **Ejercicio Práctico**

1. Crea una lista con los nombres de 5 amigos.
2. Imprime el tercer amigo de la lista.
3. Agrega un nuevo amigo al final.
4. Elimina el primer amigo de la lista.
5. Recorre la lista con un bucle e imprime cada nombre en mayúsculas.

```python
amigos = ["Carlos", "Ana", "Luis", "Pedro", "Marta"]
print(amigos[2])
amigos.append("Sofía")
del amigos[0]

for amigo in amigos:
    print(amigo.upper())
```

---

### 🎯 **Conclusión:**
- Las listas permiten almacenar y manipular colecciones de datos.
- Se pueden modificar, recorrer y ordenar con facilidad.
- Los bucles `for` y `while` facilitan el trabajo con listas.

📌 **Siguiente Clase: Tuplas y Diccionarios en Python.**


------------------------------------
# Clase 8
# **Clase 8: Tuplas y Conjuntos en Python**

## **1. Diferencias entre Listas y Tuplas**

### **Listas:**
- Son mutables (pueden modificarse después de su creación).
- Se definen con `[]` (corchetes).
- Se pueden agregar, eliminar o cambiar elementos.

```python
lista = [1, 2, 3, 4]
lista[1] = 99  # Modifica el segundo elemento
print(lista)  # [1, 99, 3, 4]
```

### **Tuplas:**
- Son inmutables (no pueden modificarse después de su creación).
- Se definen con `()` (paréntesis).
- Son más eficientes en términos de memoria y rendimiento.

```python
tupla = (1, 2, 3, 4)
print(tupla[1])  # 2
# tupla[1] = 99  # Esto generará un error porque las tuplas son inmutables.
```

### **¿Cuándo usar listas y cuándo usar tuplas?**
- Usa **listas** cuando necesites modificar los datos.
- Usa **tuplas** cuando los datos no deban cambiar y necesites mejor rendimiento.

---

## **2. Operaciones con Tuplas**

1. **Acceder a elementos**
```python
tupla = (10, 20, 30)
print(tupla[0])  # 10
```

2. **Desempaquetado de tuplas**
```python
a, b, c = tupla
print(a, b, c)  # 10 20 30
```

3. **Concatenación de tuplas**
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)  # (1, 2, 3, 4, 5, 6)
```

4. **Conversión entre lista y tupla**
```python
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)  # (1, 2, 3)
```

---

## **3. Operaciones con Conjuntos**

### **¿Qué es un conjunto?**
- Un conjunto es una colección de elementos **únicos**.
- Se define con `{}` (llaves) o con `set()`.
- No mantiene un orden específico.

```python
conjunto = {1, 2, 3, 4, 4, 2}
print(conjunto)  # {1, 2, 3, 4} (elimina duplicados)
```

### **Principales operaciones con conjuntos**

1. **Agregar elementos**
```python
conjunto.add(5)
print(conjunto)  # {1, 2, 3, 4, 5}
```

2. **Eliminar elementos**
```python
conjunto.remove(2)  # Elimina el 2
print(conjunto)  # {1, 3, 4, 5}
```

3. **Operaciones matemáticas con conjuntos**

- **Unión (`|`)**: Combina los elementos de dos conjuntos.
- **Intersección (`&`)**: Encuentra los elementos comunes.
- **Diferencia (`-`)**: Elementos que están en un conjunto pero no en otro.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Unión: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersección: {3, 4}
print(A - B)  # Diferencia: {1, 2}
```

---

## **4. Ejercicios Prácticos**

1. **Crea una tupla con 5 elementos y accede al tercer elemento.**
2. **Convierte una lista a tupla y viceversa.**
3. **Crea dos conjuntos y realiza las operaciones de unión, intersección y diferencia.**
4. **Añade y elimina elementos en un conjunto.**

---

¡Con esto ya dominas tuplas y conjuntos en Python! 🚀

-----------------------------
# Clase 9

Aquí tienes la Clase 9 sobre **Diccionarios en Python**:  

---

# **Clase 9: Diccionarios en Python**  

## **1. ¿Qué es un Diccionario en Python?**  
Un diccionario es una estructura de datos que permite almacenar pares de **clave-valor**, similar a un diccionario real donde cada palabra (clave) tiene su significado (valor).  

- Se define con llaves `{}`.  
- Cada elemento tiene una clave única que apunta a un valor.  
- Se pueden modificar, agregar o eliminar elementos.  

Ejemplo de un diccionario:  
```python
# Crear un diccionario con datos de una persona
persona = {
    "nombre": "Danny",
    "edad": 30,
    "ciudad": "Bogotá"
}
print(persona)
```
**Salida:**  
```
{'nombre': 'Danny', 'edad': 30, 'ciudad': 'Bogotá'}
```

---

## **2. Acceder a los valores de un diccionario**  
Podemos acceder a un valor usando su clave entre corchetes `[]` o con el método `.get()`.  

```python
# Accediendo a valores
print(persona["nombre"])  # Danny
print(persona.get("edad"))  # 30
```

Si intentamos acceder a una clave que no existe con `[]`, Python dará un error. Para evitarlo, `get()` devuelve `None` si la clave no está.  

```python
print(persona.get("altura", "No especificado"))  # No especificado
```

---

## **3. Modificar un Diccionario**  
Podemos cambiar un valor accediendo a su clave y asignándole un nuevo valor.  

```python
persona["edad"] = 31  # Modificar la edad
persona["profesion"] = "Programador"  # Agregar una nueva clave
print(persona)
```
**Salida:**  
```
{'nombre': 'Danny', 'edad': 31, 'ciudad': 'Bogotá', 'profesion': 'Programador'}
```

---

## **4. Eliminar elementos de un Diccionario**  
Podemos eliminar elementos usando `del`, `.pop()` o `.popitem()`.  

```python
del persona["ciudad"]  # Eliminar 'ciudad'
print(persona)

edad = persona.pop("edad")  # Elimina 'edad' y la almacena en una variable
print(edad)

ultima = persona.popitem()  # Elimina el último elemento agregado
print(ultima)
```

---

## **5. Recorrer un Diccionario con un Bucle**  
Podemos usar `for` para recorrer claves, valores o ambos.  

```python
# Iterar sobre claves
for clave in persona:
    print(clave, ":", persona[clave])

# Iterar sobre valores
for valor in persona.values():
    print(valor)

# Iterar sobre claves y valores
for clave, valor in persona.items():
    print(clave, ":", valor)
```

---

## **6. Diccionarios Anidados**  
Un diccionario puede contener otros diccionarios.  

```python
usuarios = {
    "usuario1": {"nombre": "Ana", "edad": 25},
    "usuario2": {"nombre": "Carlos", "edad": 28}
}

print(usuarios["usuario1"]["nombre"])  # Ana
```

---

## **7. Ejercicios Prácticos**  

### **Ejercicio 1:**  
Crea un diccionario con información de un libro (título, autor, año) e imprime sus valores.  

### **Ejercicio 2:**  
Modifica el diccionario para agregar un nuevo dato (número de páginas) y luego elimínalo.  

### **Ejercicio 3:**  
Crea un diccionario que almacene nombres de países y sus capitales. Luego, usa un bucle para imprimir cada país con su capital.  

---

Esto cubre los fundamentos de **Diccionarios en Python**. 🚀 ¡Practica y sigamos avanzando!  


-----------------------
# Clase 10