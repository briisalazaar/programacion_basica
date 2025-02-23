def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Se devuelve el índice donde se encontró el valor
    return -1  # Si no se encuentra el valor, se devuelve -1

# Ejemplo de uso:
lista = [5, 3, 7, 1, 9, 2]
valor_a_buscar = 7
indice = busqueda_lineal(lista, valor_a_buscar)
if indice != -1:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {indice}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")
