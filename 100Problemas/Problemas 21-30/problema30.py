#Código para calcular el factorial
def factorial(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)

# Solicitar entrada al usuario
numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")


#Código para calcular la suma de los elementos de una lista
def suma_lista(lista):
    # Caso base: si la lista está vacía, la suma es 0
    if not lista:
        return 0
    else:
        # Llamada recursiva: sumar el primer elemento y la suma del resto de la lista
        return lista[0] + suma_lista(lista[1:])

# Solicitar entrada al usuario
numeros = list(map(int, input("Ingresa los números separados por espacios: ").split()))
resultado = suma_lista(numeros)
print(f"La suma de los elementos de la lista es: {resultado}")


#Código para realizar una búsqueda binaria:
def busqueda_binaria(lista, valor, izquierda, derecha):
    # Caso base: el valor no está presente
    if izquierda > derecha:
        return -1
    
    # Encontrar el índice medio
    medio = (izquierda + derecha) // 2

    # Caso base: encontramos el valor
    if lista[medio] == valor:
        return medio
    elif lista[medio] > valor:
        # Buscar en la mitad izquierda
        return busqueda_binaria(lista, valor, izquierda, medio - 1)
    else:
        # Buscar en la mitad derecha
        return busqueda_binaria(lista, valor, medio + 1, derecha)

# Solicitar entrada al usuario
lista = sorted(list(map(int, input("Ingresa una lista de números ordenados (separados por espacios): ").split())))
valor = int(input("Ingresa el valor a buscar: "))
resultado = busqueda_binaria(lista, valor, 0, len(lista) - 1)

if resultado != -1:
    print(f"El valor {valor} se encuentra en el índice {resultado}.")
else:
    print(f"El valor {valor} no se encuentra en la lista.")


