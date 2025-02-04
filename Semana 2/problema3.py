def factorial(n):
    if n == 0:  # El factorial de 0 es 1
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i  # Multiplica cada número hasta n
        return resultado

# Solicitar al usuario el número
num = int(input("Ingresa un número para calcular su factorial: "))

# Verificar si el número es negativo
if num < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    print(f"El factorial de {num} es {factorial(num)}")
