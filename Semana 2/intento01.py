# Quiero hacer un prototipo de programa que maneje 
# una tienda online

# crearemos un diccionario de productos

# Prototipo de tienda online con buscador de productos

# Prototipo de tienda online con búsqueda flexible

# Diccionario de productos
productos = {
    "Camiseta Vshort": {"precio": 29900, "stock": 12, "promo": False},
    "Pantalon Vshort corto": {"precio": 49900, "stock": 12, "promo": False},
    "Pulsera Vshort": {"precio": 19900, "stock": 36, "promo": True},
    "Camiseta Deportiva": {"precio": 39900, "stock": 8, "promo": True}
}

def buscar_productos(termino):
    """Busca productos que contengan el término ingresado y muestra sus detalles."""
    resultados = {
        nombre: detalles for nombre, detalles in productos.items() 
        if termino.lower() in nombre.lower()
    }
    
    if resultados:
        print("\n🔎 Productos encontrados:")
        for nombre, detalles in resultados.items():
            print(f"\n📦 Producto: {nombre}")
            for clave, valor in detalles.items():
                print(f"{clave.capitalize()}: {valor}")
    else:
        print("\n⚠️ No se encontraron productos con ese término.")

# Simulación del input de búsqueda
termino_busqueda = input("\n🔍 Ingrese el nombre o categoría del producto que desea buscar: ").strip()

# Buscar y mostrar resultados
buscar_productos(termino_busqueda)

