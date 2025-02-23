def generar_pares_impares(limite):
    # Listas para almacenar los números pares e impares
    pares = []
    impares = []

    for i in range(1, limite + 1):
        if i % 2 == 0:
            pares.append(i)  # Si el número es par, lo añadimos a la lista de pares
        else:
            impares.append(i)  # Si el número es impar, lo añadimos a la lista de impares

    return pares, impares

# Solicitar al usuario el límite
limite = int(input("Ingresa el límite hasta donde generar los números: "))

# Generar las listas de números pares e impares
pares, impares = generar_pares_impares(limite)

# Mostrar los resultados
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")
