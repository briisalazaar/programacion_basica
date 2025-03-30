#Ejercicio 7: Ordenamiento y Búsqueda

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

lista = [5, 3, 8, 6, 2, 7, 4, 1]
print("Lista original:", lista)
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)
numero_a_buscar = int(input("Ingrese un número a buscar en la lista: "))
indice = binary_search(lista_ordenada, numero_a_buscar)
if indice != -1:
    print(f"Número {numero_a_buscar} encontrado en el índice {indice}.")
else:
    print(f"Número {numero_a_buscar} no encontrado en la lista.")

#Fin del ejercicio 7