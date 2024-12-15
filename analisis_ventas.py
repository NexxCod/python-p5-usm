import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
archivo_csv = "ventas_productos.csv"
df = pd.read_csv(archivo_csv)

# Calcular el precio total por producto (Cantidad * Precio)
df['Precio_Total'] = df['Cantidad'] * df['Precio']
print("Datos con Precio Total calculado:")
print(df)