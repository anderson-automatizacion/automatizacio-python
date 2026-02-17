import pandas as pd 
import os
archivo = input("Ingrese nombre del archivo Excel: ")
df = pd.read_excel(archivo)
os.makedirs("reporte_filtrado", exist_ok=True)
df_filtrado = df[df["Ventas"] > 1000]
ruta = "reporte_filtrado/reporte_filtrado.xlsx"
df_filtrado.to_excel(ruta, index=False)
print("Reporte creado correctamente")
