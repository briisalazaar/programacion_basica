#Ejercicio 3: Gestión de Contactos con Tuplas y Estructuras Anidadas

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado exitosamente.")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")


    encontrado = False
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
            encontrado = True
            break
    if not encontrado:
        print(f"Contacto '{nombre}' no encontrado en la agenda.")


def listar_contactos(agenda):
    agenda_ordenada = sorted(agenda, key=lambda x: x[0].lower())

    print("Lista de contactos:")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")


def main():
    agenda = []  # Lista para almacenar los contactos
    
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            buscar_contacto(agenda)
        elif opcion == '3':
            listar_contactos(agenda)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#Fin del ejercicio 3
