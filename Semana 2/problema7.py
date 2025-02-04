def es_par(num):
    return num % 2 == 0
def es_impar(num):
    return num % 2 != 0
def es_multiplo(num, divisor):
    return num % divisor == 0

# Solicitar al usuario los números
num = int(input("Ingresa un número para verificar si es par, impar o múltiplo: "))
divisor = int(input("Ingresa el divisor para verificar si es múltiplo: "))

# Verificar si el número es par o impar
if es_par(num):
    print(f"{num} es un número par.")
else:
    print(f"{num} es un número impar.")

# Verificar si el número es múltiplo del divisor
if es_multiplo(num, divisor):
    print(f"{num} es múltiplo de {divisor}.")
else:
    print(f"{num} no es múltiplo de {divisor}.")
