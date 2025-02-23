# Definimos la agenda como un diccionario vacío
agenda = {}

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    
    # Agregar el contacto a la agenda
    agenda[nombre] = {'telefono': telefono, 'correo': correo}
    print(f"Contacto {nombre} agregado exitosamente.")

# Función para mostrar todos los contactos
def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\nLista de contactos:")
        for nombre, detalles in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"  Teléfono: {detalles['telefono']}")
            print(f"  Correo: {detalles['correo']}")
            print("-" * 20)

# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre}")
        print(f"  Teléfono: {agenda[nombre]['telefono']}")
        print(f"  Correo: {agenda[nombre]['correo']}")
    else:
        print(f"No se encontró el contacto con el nombre {nombre}.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado exitosamente.")
    else:
        print(f"No se encontró el contacto con el nombre {nombre}.")

# Función principal para mostrar el menú y gestionar la agenda
def menu():
    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            mostrar_contactos()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
