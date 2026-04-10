#open para abrir el archivo
archivo = open ("archivos\\texto_de_xavi.txt")
#Leer archivo completo
#archivoC = archivo.read()

#Leer linea por linea
#lineas = archivo.readlines()


#Leer una sola linea 
linea = archivo.readline()
print(linea)

#cerrar el archivo
archivo.close()