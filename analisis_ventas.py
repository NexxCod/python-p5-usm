import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
archivo_csv = "ventas_productos.csv"
df = pd.read_csv(archivo_csv)

# Calcular el precio total por producto (Cantidad * Precio)
df['Precio_Total'] = df['Cantidad'] * df['Precio']
print("Datos con Precio Total calculado:")
print(df)

# Crear un gráfico de barras que muestre el Precio Total por Producto
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
plt.bar(df['Producto'], df['Precio_Total'])
plt.title('Precio Total por Producto')
plt.xlabel('Producto')
plt.ylabel('Precio Total')

# Guardar el gráfico como imagen PNG
plt.savefig('precio_total_productos.png')

# Mostrar el gráfico
plt.show()

