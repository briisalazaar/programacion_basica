def interes_compuesto(P, r, n, t):
    A = P * (1 + r/n) ** (n * t)  # Fórmula del interés compuesto
    return A

# Solicitar al usuario los datos
P = float(input("Ingresa el capital inicial (P): "))
r = float(input("Ingresa la tasa de interés anual (r) en porcentaje: ")) / 100  # Convertir a decimal
n = int(input("Ingresa el número de veces que se capitaliza el interés por año (n): "))
t = float(input("Ingresa el tiempo en años (t): "))

# Calcular el monto final
A = interes_compuesto(P, r, n, t)

# Calcular los intereses generados
intereses = A - P

# Mostrar los resultados
print(f"Monto final (A): {A:.2f}")
print(f"Intereses generados: {intereses:.2f}")
