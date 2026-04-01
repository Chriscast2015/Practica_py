#creando conjunto con set()

conjunto = set(["Dato1","Dato2","Dato3"])


#Conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato1", "Dato2"])
conjunto2 = {conjunto1, "Dato3"}
print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {8}

#subconjunto 
#resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 <= conjunto1

#superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto1 > conjunto2
#print(resultado)

#verificar si hay un numero en comun 
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)