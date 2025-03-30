#Ejercicio 4: Calculadora de Estadísticas

def calcular_estadisticas(*args):
    # Calcular promedio
    promedio = sum(args) / len(args) if args else 0
    # Calcular mediana
    sorted_args = sorted(args)
    n = len(sorted_args)
    if n % 2 == 0:
        mediana = (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2
    else:
        mediana = sorted_args[n // 2]
    # Calcular desviación estándar
    media = lambda x: sum(x) / len(x)
    varianza = sum((x - media(args)) ** 2 for x in args) / len(args)
    desviacion_estandar = varianza ** 0.5

    return promedio, mediana, desviacion_estandar


# Solicitar al usuario una lista de números
numeros = input("Introduce una lista de números separados por comas: ")
numeros = [float(num) for num in numeros.split(",")]

# Llamar a la función y mostrar los resultados
promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion_estandar}")

#Fin del Ejercicio 4
