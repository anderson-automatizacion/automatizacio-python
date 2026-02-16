import pandas as pd
import os

# Crear carpeta si no existe
os.makedirs("reporte_filtrado", exist_ok=True)

# Leer archivo Excel
df = pd.read_excel("datos.xlsx.xlsx")

# Ver columnas reales
print("Columnas encontradas:")
print(df.columns)

# Filtrar datos
df_filtrado = df[df["VENTAS"] > 1000]

# Guardar archivo
ruta = "reporte_filtrado/reporte_filtrado.xlsx"
df_filtrado.to_excel(ruta, index=False)

print("Reporte creado correctamente")