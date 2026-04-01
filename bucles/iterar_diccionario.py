diccionario = {
    'nombre' : "Christian",
    "Apellido" : 'Castro',
    'Edad': 20
}

for claves in diccionario:
    print(claves)
    


#recorriendo diccionario con items() key, value 
for datos in diccionario.items():
    key = datos[0]
    values = datos[1]
    print(f"Clave: {key}, Valor: {values}")