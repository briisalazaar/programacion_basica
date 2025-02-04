def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(n**0.5) + 1):  # Solo comprobamos hasta la raíz cuadrada de n
        if n % i == 0:  # Si n es divisible por i, no es primo
            return False
    return True  # Si no es divisible por ningún número, es primo

# Solicitar al usuario el número
num = int(input("Ingresa un número para verificar si es primo: "))

# Verificar si el número es primo
if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
