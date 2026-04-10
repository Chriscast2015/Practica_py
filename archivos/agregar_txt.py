with open("archivos\\texto_de_xavi.txt","a",encoding="UTF-8") as archivo:
    
    #agregando archivo 
    #archivo.write("jajjajaj")
    
    archivo.write("\n")
    #usando un bucle para gregar varias lineas 
    for i in range(5):
        archivo.write(f"linea {i+1} agregada\n")