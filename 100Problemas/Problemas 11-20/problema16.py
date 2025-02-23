def contar_vocales_consonantes(cadena):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    # Inicializar los contadores
    vocales_contador = 0
    consonantes_contador = 0
    
    # Recorrer cada caracter de la cadena
    for char in cadena:
        if char.isalpha():  # Verificar si el carácter es una letra
            if char in vocales:
                vocales_contador += 1
            else:
                consonantes_contador += 1
    
    return vocales_contador, consonantes_contador

# Solicitar al usuario que ingrese una cadena
cadena = input("Introduce una cadena de texto: ")

# Contar vocales y consonantes
vocales, consonantes = contar_vocales_consonantes(cadena)

# Mostrar el resultado
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
