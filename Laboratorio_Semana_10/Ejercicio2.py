#Ejercicio 2: Manejo de Inventario con Listas y Diccionarios

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    inventario[nombre] = {'categoria': categoria, 'precio': precio, 'cantidad': cantidad}
    print(f"Producto '{nombre}' agregado al inventario.")
    


def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Producto encontrado: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


def mostrar_inventario_ordenado(inventario):
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]['precio'])

    print("Productos ordenados por precio (menor a mayor):")
    for nombre, producto in productos_ordenados:
        print(f"Nombre: {nombre}, Categoría: {producto['categoria']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def main():
    inventario = {}
    
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar inventario ordenado por precio")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            eliminar_producto(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            mostrar_inventario_ordenado(inventario)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
    
#Fin del ejercicio 2