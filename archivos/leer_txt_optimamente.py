#abriendo archivo con with open
with open("archivos\\texto_de_xavi.txt") as archivo:
    #leemos el archivo con .read
    contenido = archivo.read()
    
    #mostramos el archivo 
    print(contenido)
    
#no es necesario cerrar el archivo con with open