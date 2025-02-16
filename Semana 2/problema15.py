# Función para determinar si un año es bisiesto
def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Solicitar al usuario que ingrese un año
año = int(input("Introduce un año para verificar si es bisiesto: "))

# Verificar si el año es bisiesto y mostrar el resultado
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
