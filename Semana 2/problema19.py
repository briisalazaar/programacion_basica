
import random

def menu():
    print("\n--- Generador de Números Aleatorios con Distintas Distribuciones ---")
    print("1. Distribución Uniforme")
    print("2. Distribución Normal")
    print("3. Distribución Exponencial")
    print("4. Distribución Binomial")
    print("5. Distribución de Poisson")
    print("6. Distribución Beta")
    print("7. Distribución de Cauchy")
    print("8. Salir")

def distribucion_uniforme():
    a = float(input("Introduce el límite inferior a: "))
    b = float(input("Introduce el límite superior b: "))
    numero = random.uniform(a, b)
    print(f"Número aleatorio con distribución uniforme entre {a} y {b}: {numero}")

def distribucion_normal():
    media = float(input("Introduce la media (mu): "))
    desviacion_estandar = float(input("Introduce la desviación estándar (sigma): "))
    numero = random.gauss(media, desviacion_estandar)
    print(f"Número aleatorio con distribución normal (media={media}, desviación estándar={desviacion_estandar}): {numero}")

def distribucion_exponencial():
    lambda_ = float(input("Introduce la tasa (lambda): "))
    numero = random.expovariate(lambda_)
    print(f"Número aleatorio con distribución exponencial (lambda={lambda_}): {numero}")

def distribucion_binomial():
    n = int(input("Introduce el número de intentos n: "))
    p = float(input("Introduce la probabilidad de éxito p: "))
    numero = random.binomial(n, p)
    print(f"Número aleatorio con distribución binomial (n={n}, p={p}): {numero}")

def distribucion_poisson():
    lambda_ = float(input("Introduce la tasa promedio de ocurrencias lambda: "))
    numero = random.poisson(lambda_)
    print(f"Número aleatorio con distribución de Poisson (lambda={lambda_}): {numero}")

def distribucion_beta():
    alpha = float(input("Introduce el parámetro alpha: "))
    beta = float(input("Introduce el parámetro beta: "))
    numero = random.betavariate(alpha, beta)
    print(f"Número aleatorio con distribución beta (alpha={alpha}, beta={beta}): {numero}")

def distribucion_cauchy():
    numero = random.standard_cauchy()
    print(f"Número aleatorio con distribución de Cauchy: {numero}")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-7, 8 para salir): ")

        if opcion == "1":
            distribucion_uniforme()
        elif opcion == "2":
            distribucion_normal()
        elif opcion == "3":
            distribucion_exponencial()
        elif opcion == "4":
            distribucion_binomial()
        elif opcion == "5":
            distribucion_poisson()
        elif opcion == "6":
            distribucion_beta()
        elif opcion == "7":
            distribucion_cauchy()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 8.")

if __name__ == "__main__":
    main()
