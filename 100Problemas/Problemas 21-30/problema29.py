import numpy as np # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Generar datos aleatorios (por ejemplo, 1000 datos de ingresos de personas)
np.random.seed(42)  # Para reproducir resultados
ingresos = np.random.normal(loc=50000, scale=15000, size=1000)  # Media 50000, desviación estándar 15000

# Crear un DataFrame de Pandas con los datos generados
df = pd.DataFrame(ingresos, columns=["Ingreso"])

# Mostrar algunas estadísticas básicas
media = df["Ingreso"].mean()
mediana = df["Ingreso"].median()
desviacion = df["Ingreso"].std()
minimo = df["Ingreso"].min()
maximo = df["Ingreso"].max()

# Mostrar las estadísticas
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion}")
print(f"Valor Mínimo: {minimo}")
print(f"Valor Máximo: {maximo}")

# Análisis de la distribución de los datos
# Histograma para ver la distribución de los ingresos
plt.hist(df["Ingreso"], bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de los Ingresos")
plt.xlabel("Ingreso")
plt.ylabel("Frecuencia")
plt.show()

# Caja de bigotes (boxplot) para ver los valores atípicos
plt.boxplot(df["Ingreso"], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title("Boxplot de Ingresos")
plt.xlabel("Ingreso")
plt.show()

# Análisis de correlación entre diferentes variables (en este caso solo una variable)
# Generar una segunda variable (por ejemplo, Edad)
edades = np.random.randint(18, 65, size=1000)
df["Edad"] = edades

# Calcular la correlación entre Ingreso y Edad
correlacion = df["Ingreso"].corr(df["Edad"])

# Mostrar la correlación
print(f"Correlación entre Ingreso y Edad: {correlacion}")

# Gráfico de dispersión (scatter plot) para visualizar la relación
plt.scatter(df["Edad"], df["Ingreso"], color='orange', alpha=0.5)
plt.title("Relación entre Edad e Ingreso")
plt.xlabel("Edad")
plt.ylabel("Ingreso")
plt.show()

