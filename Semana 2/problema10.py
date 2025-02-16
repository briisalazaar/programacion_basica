# Leer el contenido de un archivo de texto
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

# Escribir en un archivo de texto
def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

# Modificar el contenido de un archivo de texto
def modificar_archivo(nombre_archivo, nuevo_contenido):
    with open(nombre_archivo, 'r+') as archivo:
        contenido = archivo.read()
        # Modificar el contenido
        contenido = contenido.replace(contenido, nuevo_contenido)  # Ejemplo: reemplazar todo el contenido
        archivo.seek(0)  # Volver al inicio para sobrescribir
        archivo.write(contenido)

# Ejemplo de uso
nombre_archivo = 'archivo.txt'

# Escribir en el archivo
escribir_archivo(nombre_archivo, "Este es el nuevo contenido del archivo.")

# Leer el archivo
print("Contenido original del archivo:")
print(leer_archivo(nombre_archivo))

# Modificar el archivo
modificar_archivo(nombre_archivo, "Este es el contenido modificado del archivo.")

# Leer el archivo después de modificarlo
print("Contenido después de modificar:")
print(leer_archivo(nombre_archivo))
