def mayor_entre_tres(a, b, c):
    return max(a, b, c)

# Solicitar los valores al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

# Mostrar el mayor
print("El mayor número es:", mayor_entre_tres(a, b, c))