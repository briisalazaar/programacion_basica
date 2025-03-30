#Ejercicio 5: Módulo para Conversi´on de Unidades

def km_a_millas(kilometros):
    return kilometros * 0.621371

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    return litros * 0.264172

def main():
    print("Conversor de Unidades")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == '1':
        km = float(input("Ingrese la distancia en kilómetros: "))
        millas = km_a_millas(km)
        print(f"{km} kilómetros son {millas} millas.")
    elif opcion == '2':
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif opcion == '3':
        litros = float(input("Ingrese el volumen en litros: "))
        galones = litros_a_galones(litros)
        print(f"{litros} litros son {galones} galones.")
    else:
        print("Opción no válida. Intente nuevamente.")

#Fin ejercicio 5