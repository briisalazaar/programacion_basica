import math

# Cálculo del área de diferentes figuras geométricas

# 1. Área de un círculo
# Fórmula: Área = pi * radio^2
def area_circulo(radio):
    return math.pi * radio ** 2

# 2. Área de un rectángulo
# Fórmula: Área = largo * ancho
def area_rectangulo(largo, ancho):
    return largo * ancho

# 3. Área de un triángulo
# Fórmula: Área = (base * altura) / 2
def area_triangulo(base, altura):
    return (base * altura) / 2

# Cálculo del volumen de diferentes figuras geométricas

# 4. Volumen de un cubo
# Fórmula: Volumen = lado^3
def volumen_cubo(lado):
    return lado ** 3

# 5. Volumen de una esfera
# Fórmula: Volumen = (4/3) * pi * radio^3
def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

# Aquí pedimos los datos al usuario y mostramos los resultados

# 1. Cálculo del área de un círculo
print("Cálculo del área de un círculo")
radio = float(input("Ingresa el radio del círculo: "))
area_c = area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area_c:.2f}\n")

# 2. Cálculo del área de un rectángulo
print("Cálculo del área de un rectángulo")
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area_r = area_rectangulo(largo, ancho)
print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area_r:.2f}\n")

# 3. Cálculo del área de un triángulo
print("Cálculo del área de un triángulo")
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area_t = area_triangulo(base, altura)
print(f"El área del triángulo con base {base} y altura {altura} es: {area_t:.2f}\n")

# 4. Cálculo del volumen de un cubo
print("Cálculo del volumen de un cubo")
lado = float(input("Ingresa el lado del cubo: "))
volumen_c = volumen_cubo(lado)
print(f"El volumen del cubo con lado {lado} es: {volumen_c:.2f}\n")

# 5. Cálculo del volumen de una esfera
print("Cálculo del volumen de una esfera")
radio_esfera = float(input("Ingresa el radio de la esfera: "))
volumen_e = volumen_esfera(radio_esfera)
print(f"El volumen de la esfera con radio {radio_esfera} es: {volumen_e:.2f}")
