# Función para mostrar una matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para pedir una matriz al usuario
def pedir_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento en la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para sumar dos matrices
def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    matriz_resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        matriz_resultado.append(fila_resultado)
    
    return matriz_resultado

# Función para restar dos matrices
def resta_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    
    matriz_resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] - matriz2[i][j])
        matriz_resultado.append(fila_resultado)
    
    return matriz_resultado

# Función para multiplicar dos matrices
def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda")
    
    matriz_resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        matriz_resultado.append(fila_resultado)
    
    return matriz_resultado

# Función para transponer una matriz
def transponer_matriz(matriz):
    matriz_transpuesta = []
    for j in range(len(matriz[0])):
        fila_transpuesta = []
        for i in range(len(matriz)):
            fila_transpuesta.append(matriz[i][j])
        matriz_transpuesta.append(fila_transpuesta)
    
    return matriz_transpuesta

# Solicitar dimensiones de las matrices
filas_A = int(input("Ingresa el número de filas de la matriz A: "))
columnas_A = int(input("Ingresa el número de columnas de la matriz A: "))
matriz_A = pedir_matriz(filas_A, columnas_A)

filas_B = int(input("Ingresa el número de filas de la matriz B: "))
columnas_B = int(input("Ingresa el número de columnas de la matriz B: "))
matriz_B = pedir_matriz(filas_B, columnas_B)

# Mostrar las matrices
print("\nMatriz A:")
mostrar_matriz(matriz_A)

print("\nMatriz B:")
mostrar_matriz(matriz_B)

# Realizar las operaciones y mostrar los resultados

# Suma de matrices
if len(matriz_A) == len(matriz_B) and len(matriz_A[0]) == len(matriz_B[0]):
    print("\nSuma de A y B:")
    resultado_suma = suma_matrices(matriz_A, matriz_B)
    mostrar_matriz(resultado_suma)
else:
    print("\nLas matrices A y B no tienen las mismas dimensiones, no se puede realizar la suma.")

# Resta de matrices
if len(matriz_A) == len(matriz_B) and len(matriz_A[0]) == len(matriz_B[0]):
    print("\nResta de A y B:")
    resultado_resta = resta_matrices(matriz_A, matriz_B)
    mostrar_matriz(resultado_resta)
else:
    print("\nLas matrices A y B no tienen las mismas dimensiones, no se puede realizar la resta.")

# Multiplicación de matrices
if len(matriz_A[0]) == len(matriz_B):
    print("\nMultiplicación de A y B:")
    resultado_multiplicacion = multiplicar_matrices(matriz_A, matriz_B)
    mostrar_matriz(resultado_multiplicacion)
else:
    print("\nEl número de columnas de la matriz A no es igual al número de filas de la matriz B, no se puede realizar la multiplicación.")

# Transposición de la matriz A
print("\nTransposición de la matriz A:")
resultado_transpuesta = transponer_matriz(matriz_A)
mostrar_matriz(resultado_transpuesta)
