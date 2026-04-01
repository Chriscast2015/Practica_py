frutas = ["Manzana", "Pera", "Naranja", "Banana"]


#Evitando que se coma una pera con la sentencia continue
for fruta in frutas:
    if fruta == 'Pera':
        continue
    print(f"Ejecutando el bucle, fruta actual: {fruta}")
else:
    print("Bucle terminado")
    
    
#Evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == 'Pera':
        break
    print(f"Ejecutando el bucle, fruta actual: {fruta}")
else:
    print("Bucle terminado")
    
#iterar cadenas de texto
nombres = "Christian"

for nombre in nombres:
    print(nombre) 
    
    
numeros = [1,2,3,4,5]

numeros_duplicados =[x*2 for x in numeros]
print(numeros_duplicados)
