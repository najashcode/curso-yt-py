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

Con esto concluye la primera clase. ¡Estás listo para explorar más de Python!

perfecto! he terminado la primera clase, dame ejercicios para practicar


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

Con esto concluye la segunda clase. ¡Practica y sigue aprendiendo Python!

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

---

Con esto concluye la tercera clase. ¡Practica combinando operadores para resolver problemas complejos!

