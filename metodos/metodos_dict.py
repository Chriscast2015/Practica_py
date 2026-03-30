diccionario = {
    "nombre": "Christian",
    "Apellido": "Castro",
    "Edad": 20
}

#obteniendo un elelmento con get    
claves = diccionario.get("")


#eliminando todo el diccionario
#diccionario.clear()

diccionario.pop("nombre")
print(diccionario)

diccionario_iterable = diccionario.items()
print(diccionario_iterable)