#contar pares e impares

pares = 0
impares = 0

for i in range(1,11):
    if i % 2 == 0:
        pares += 1
    
    else:
        impares +=1
        
print(f"Pares: {pares}")
print(f"Impares: {impares}")
 
    
