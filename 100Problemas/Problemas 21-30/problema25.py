import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Función para generar un histograma
def generar_histograma(datos, bins=10):
    # Generar el histograma
    plt.hist(datos, bins=bins, color='blue', edgecolor='black')
    
    # Etiquetas y título
    plt.title('Histograma de Datos')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')

    # Mostrar el histograma
    plt.show()

# Pedir datos al usuario
n = int(input("¿Cuántos datos quieres ingresar? "))
datos = []

for i in range(n):
    valor = float(input(f"Ingrese el dato #{i+1}: "))
    datos.append(valor)

# Convertir la lista a un array de NumPy (opcional pero recomendado para trabajar con datos numéricos)
datos = np.array(datos)

# Generar el histograma con los datos ingresados
generar_histograma(datos)


