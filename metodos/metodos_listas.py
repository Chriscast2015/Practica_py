lista = list([5,6,4,1,True])

#devuelve la cantidad de elementos de la lista
len_lista = len(lista)

#agrega elementos a la lista 
lista.append(2)

#agrega elemento con un indice especifico
#lista.insert() 

#agrega dos elementos a la lista
lista.extend([True,25.2 ])

#eliminando por su indice
#lista.pop(-1)

#remueve un elemento por su valor
lista.remove(True)

#elimina toda la lista
#lista.clear()
#ordena
lista.sort()

#reversa el orden de la lista
lista.reverse()
print(lista)