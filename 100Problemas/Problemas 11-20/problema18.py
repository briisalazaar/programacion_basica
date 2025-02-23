import cmath  # Para manejar números complejos

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Calcular las dos soluciones (reales o complejas)
    sol1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    sol2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    
    return sol1, sol2

# Solicitar los coeficientes al usuario
print("Resuelve la ecuación cuadrática ax^2 + bx + c = 0")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Verificar si a es cero (no sería una ecuación cuadrática)
if a == 0:
    print("No es una ecuación cuadrática (a no puede ser cero).")
else:
    soluciones = resolver_ecuacion_cuadratica(a, b, c)
    print(f"Las soluciones de la ecuación son: {soluciones[0]} y {soluciones[1]}")
