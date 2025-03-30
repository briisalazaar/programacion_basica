#Ejercicio 1: Análisis de Texto con Diccionarios y Conjuntos

texto = input("Ingrese un texto: ")

# Convertir el texto a minúsculas y eliminar signos de puntuación
import string
texto = texto.lower().translate(str.maketrans("", "", string.punctuation))

# Dividir el texto en palabras
palabras = texto.split()

# Contar el número total de palabras
num_palabras = len(palabras)

# Contar la cantidad de palabras únicas usando un conjunto
palabras_unicas = set(palabras)
num_palabras_unicas = len(palabras_unicas)

# Contar la frecuencia de cada palabra usando un diccionario
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Encontrar la palabra más frecuente y cuántas veces aparece
frecuencia_maxima = max(frecuencia_palabras.values())
palabra_mas_frecuente = [palabra for palabra, frecuencia in frecuencia_palabras.items() if frecuencia == frecuencia_maxima]
palabra_mas_frecuente = palabra_mas_frecuente[0]  # Tomar la primera en caso de empate

# Mostrar el resumen
print("\nResumen del análisis de texto:")
print(f"Número total de palabras: {num_palabras}")
print(f"Cantidad de palabras únicas: {num_palabras_unicas}")
print(f"Frecuencia de palabras: {frecuencia_palabras}")
print(f"Palabra más frecuente: '{palabra_mas_frecuente}' ({frecuencia_maxima} veces)")

# Fin del ejercicio 1