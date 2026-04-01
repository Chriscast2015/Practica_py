animales = ["perro","gato","conejo","cangrejo"]
numeros = [1,2,3,4]
for animal in animales:
    print(animal)
    
for numero in numeros:
    resultado = numero *10
    print(resultado)
    
for animal,numero in zip(animales,numeros):
    print(f'lista animal: {animal} lista 2 numero: {numero}')
    
    
for num in range(0, 2):
    print(num)

#recorrer con índice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
    
    
#usando else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero}")
else:
    print("Bucle terminado")
    
#funciona para listas, tuplas, conjuntos