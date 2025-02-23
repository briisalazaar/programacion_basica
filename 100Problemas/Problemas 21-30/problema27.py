# Funciones de conversión

# Longitud (m -> km, m -> millas, etc.)
def convertir_longitud(valor, de, a):
    if de == 'm' and a == 'km':
        return valor / 1000
    elif de == 'm' and a == 'millas':
        return valor * 0.000621371
    elif de == 'km' and a == 'm':
        return valor * 1000
    elif de == 'km' and a == 'millas':
        return valor * 0.621371
    elif de == 'millas' and a == 'm':
        return valor / 0.000621371
    elif de == 'millas' and a == 'km':
        return valor / 0.621371
    else:
        return "Conversión no disponible"

# Temperatura (C -> F, C -> K, etc.)
def convertir_temperatura(valor, de, a):
    if de == 'C' and a == 'F':
        return valor * 9/5 + 32
    elif de == 'C' and a == 'K':
        return valor + 273.15
    elif de == 'F' and a == 'C':
        return (valor - 32) * 5/9
    elif de == 'F' and a == 'K':
        return (valor - 32) * 5/9 + 273.15
    elif de == 'K' and a == 'C':
        return valor - 273.15
    elif de == 'K' and a == 'F':
        return (valor - 273.15) * 9/5 + 32
    else:
        return "Conversión no disponible"

# Masa (kg -> g, kg -> libras, etc.)
def convertir_masa(valor, de, a):
    if de == 'kg' and a == 'g':
        return valor * 1000
    elif de == 'kg' and a == 'libras':
        return valor * 2.20462
    elif de == 'g' and a == 'kg':
        return valor / 1000
    elif de == 'g' and a == 'libras':
        return valor * 0.00220462
    elif de == 'libras' and a == 'kg':
        return valor / 2.20462
    elif de == 'libras' and a == 'g':
        return valor / 0.00220462
    else:
        return "Conversión no disponible"

# Función principal para el menú
def menu():
    while True:
        print("\nConversor de Unidades")
        print("1. Longitud")
        print("2. Temperatura")
        print("3. Masa")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            # Conversión de Longitud
            valor = float(input("Ingrese el valor a convertir: "))
            de = input("Unidad de origen (m, km, millas): ")
            a = input("Unidad de destino (m, km, millas): ")
            resultado = convertir_longitud(valor, de, a)
            print(f"{valor} {de} es igual a {resultado} {a}")
        
        elif opcion == '2':
            # Conversión de Temperatura
            valor = float(input("Ingrese el valor a convertir: "))
            de = input("Unidad de origen (C, F, K): ")
            a = input("Unidad de destino (C, F, K): ")
            resultado = convertir_temperatura(valor, de, a)
            print(f"{valor}° {de} es igual a {resultado}° {a}")
        
        elif opcion == '3':
            # Conversión de Masa
            valor = float(input("Ingrese el valor a convertir: "))
            de = input("Unidad de origen (kg, g, libras): ")
            a = input("Unidad de destino (kg, g, libras): ")
            resultado = convertir_masa(valor, de, a)
            print(f"{valor} {de} es igual a {resultado} {a}")
        
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
