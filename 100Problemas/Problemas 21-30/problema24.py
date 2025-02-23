# Función para calcular la suma de los primeros n números naturales
def suma_serie_numeros(n):
    # Usamos la fórmula de la suma de los primeros n números naturales: n * (n + 1) / 2
    suma = n * (n + 1) // 2  # Usamos el operador // para asegurarnos de que sea un valor entero
    return suma

# Pedir al usuario el número de términos de la serie
n = int(input("Ingrese el valor de n (número de términos de la serie): "))

# Calcular y mostrar la suma
resultado = suma_serie_numeros(n)
print(f"La suma de los primeros {n} números naturales es: {resultado}")



# Función para calcular la suma de una progresión aritmética
def suma_progresion_aritmetica(a, d, n):
    # Usamos la fórmula de la suma de la progresión aritmética
    suma = n * (2 * a + (n - 1) * d) // 2  # Utilizamos // para asegurarnos de que el resultado sea entero
    return suma

# Pedir al usuario los parámetros de la progresión aritmética
a = int(input("Ingrese el primer término de la progresión (a): "))
d = int(input("Ingrese la diferencia común (d): "))
n = int(input("Ingrese el número de términos (n): "))

# Calcular y mostrar la suma
resultado = suma_progresion_aritmetica(a, d, n)
print(f"La suma de los primeros {n} términos de la progresión aritmética es: {resultado}")


