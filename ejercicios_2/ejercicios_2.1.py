#falto el profe y los alumnos va a dar clase

#pedir nombre y edad de los que vinieron a clase 

#funcion para obtener al asistente y la profesor según la edad 
def obtener_compañeros(cantidad_de_compañeros):
    #creando la lista de compañeros
    compañeros = []
    
    #ejecutando un for para pedir la informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista 
        compañeros.append(compañero)
    
    #ordenamos los numeros de menor a mayor según la edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor 

#desempaquetamos lo que nos retorna la función
asistente, profesor = obtener_compañeros(5)


#mostrando el resultado 
print(f"El profesor es: {profesor} y su asistente es {asistente}")