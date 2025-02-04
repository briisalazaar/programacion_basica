import math  # Para usar la constante pi

def area_circulo(r):
    return math.pi * r ** 2  # Fórmula para el área
def circunferencia_circulo(r):
    return 2 * math.pi * r  # Fórmula para la circunferencia

# Solicitar al usuario el radio
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área y la circunferencia
area = area_circulo(radio)
circunferencia = circunferencia_circulo(radio)

# Mostrar los resultados
print(f"Área del círculo: {area:.2f}")
print(f"Circunferencia del círculo: {circunferencia:.2f}")
