def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b  # La siguiente número en la secuencia es la suma de los dos anteriores
    return secuencia

# Solicitar al usuario el número de términos
num_term = int(input("Ingresa el número de términos de la secuencia de Fibonacci: "))

# Generar y mostrar la secuencia
if num_term <= 0:
    print("Por favor ingresa un número positivo.")
else:
    print(f"Secuencia de Fibonacci de {num_term} términos: {fibonacci(num_term)}")
