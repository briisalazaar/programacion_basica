# Funciones para convertir temperaturas entre distintas escalas

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Solicitar al usuario la temperatura y la escala de origen
print("Seleccione la escala de origen:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

escala_origen = int(input("Ingrese el número de la escala de origen: "))

# Solicitar la temperatura
temperatura = float(input("Ingrese la temperatura: "))

# Solicitar la escala de destino
print("Seleccione la escala de destino:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

escala_destino = int(input("Ingrese el número de la escala de destino: "))

# Realizar la conversión según la elección del usuario
if escala_origen == 1:  # Celsius
    if escala_destino == 1:
        print(f"{temperatura}°C es igual a {temperatura}°C")
    elif escala_destino == 2:
        print(f"{temperatura}°C es igual a {celsius_a_fahrenheit(temperatura)}°F")
    elif escala_destino == 3:
        print(f"{temperatura}°C es igual a {celsius_a_kelvin(temperatura)}K")
elif escala_origen == 2:  # Fahrenheit
    if escala_destino == 1:
        print(f"{temperatura}°F es igual a {fahrenheit_a_celsius(temperatura)}°C")
    elif escala_destino == 2:
        print(f"{temperatura}°F es igual a {temperatura}°F")
    elif escala_destino == 3:
        print(f"{temperatura}°F es igual a {fahrenheit_a_kelvin(temperatura)}K")
elif escala_origen == 3:  # Kelvin
    if escala_destino == 1:
        print(f"{temperatura}K es igual a {kelvin_a_celsius(temperatura)}°C")
    elif escala_destino == 2:
        print(f"{temperatura}K es igual a {kelvin_a_fahrenheit(temperatura)}°F")
    elif escala_destino == 3:
        print(f"{temperatura}K es igual a {temperatura}K")

