with open("archivos\\texto_de_xavi.txt","w",encoding="UTF-8") as archivo:
    
    #sobreescribiendo el archivo
    #archivo.write("jajajaja")
    
    #agregando dos lineas con writelines
    archivo.writelines(["Hola maestro\n","Cómo estás?\n"])
    
    #agregando otras dos lineas
    archivo.writelines(["bien\n","o mal?"])