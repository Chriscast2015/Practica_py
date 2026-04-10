#cambiar el tipo de dato de una columna 
import pandas as pd
df =pd.read_csv("archivos_problemas\\datos.csv")

#convertir a str los datos de una columna
df["edad"] = df["edad"].astype(str)

#mostrar el tipo de dato de la columna edad 
#print(type(df["edad"][0]))

#df["apellido"].replace("Castro","Maestro",inplace=False)
df.replace({"apellido": {"Castro": "Maestro"}}, inplace=True)

      
#Eliminando las filas con datos vacios
df = df.dropna()

#Eliminando las filas repetidas 
df=df.drop_duplicates()

#Creando un CSV con el df resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")
