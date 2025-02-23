import random

# Función para simular el lanzamiento de un dado (con 6 caras)
def lanzar_dado():
    return random.randint(1, 6)

# Función para simular el lanzamiento de una moneda
def lanzar_moneda():
    # Puede ser "Cara" o "Cruz"
    return random.choice(["Cara", "Cruz"])

# Simulamos el lanzamiento de un dado
print("Lanzamiento de un dado:")
resultado_dado = lanzar_dado()
print(f"El resultado del dado es: {resultado_dado}")

# Simulamos el lanzamiento de una moneda
print("\nLanzamiento de una moneda:")
resultado_moneda = lanzar_moneda()
print(f"El resultado de la moneda es: {resultado_moneda}")