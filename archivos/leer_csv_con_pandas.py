import pandas as pd

#función .read_csv para leer el archivo csv 
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo datos de la columna nombre
nombres = df["nombre"]

#ordenando df por edad

df_orden_ascendente = df.sort_values("edad")

#ordenadno de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con .head()

primeras_filas = df.head(1)

#accediendo a las ultimas 3 filas con .tail()
ultimas_filas = df.tail(1)

#accediendo a la cantidad de filas y columnas con shape 
#filas_y_columnas_totales = df.shape
#filas_totales = filas_y_columnas_totales[0]
#columnas_totales = filas_y_columnas_totales[1]

filas_totales,columnas_totales = df.shape

#obteniendo data estadistica ded df
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico del df con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,2]

#accediendo fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo fila 3 con iloc
fila_33 = df.iloc[2,:]

#accediendo a filas con edad > 30
mayor_que_30 = df.loc[df["edad"]<30,:]
print(mayor_que_30)


