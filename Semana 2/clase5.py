# 🟢 **1. Nesting (Anidamiento de bucles)**  

for i in range(1,4): #Bucle externo
    for j in range(1,4): #Bucle interno
        print(f"i={i}, j={j}")

# **Ejemplo 2: Dibujando un patrón con bucles anidados**

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()#Salto de linea


# **Ejemplo 3: Recorrer una lista con un bucle anidado**
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for fila in matriz:
    for elemento in fila:
        print(f"{elemento:2}", end=" ")  # Formato con alineación
    print()

productos = {
    "Laptop": {"precio": 2500, "stock": 10},
    "Teléfono": {"precio": 1200, "stock": 20},
    "Tablet": {"precio": 800, "stock": 15}
}

for producto, detalles in productos.items(): #Recorre productos y guarda en producto las claves del diccionario
    #detalle guarda sus valores
    print(f"\n📦 Producto: {producto}") #imprimo el producto 
    for clave, valor in detalles.items():# itero sobre los detalles guardando los valores en su clave y  valor correspondiente
        print(f"{clave}: {valor}") #imprimo los detalles


empleados = {
    "Juan": 28,
    "Maria": 32,
    "Carlos": 24
}

nombres = list(empleados.keys())  # Convertimos claves a lista
i = 0

while i < len(nombres):
    nombre = nombres[i]
    print(f"{nombre} tiene {empleados[nombre]} años")
    i += 1

# Ejercicios Practicos
# Matriz Cuadrada


