cadena1 = "Hola,bola,adios"
cadena2 = "bievenido"
#Mays
resultado = cadena2.upper()
#Mins
resultado = cadena2.lower()

#primera letra Mays 
primer_letra_mays = cadena2.capitalize()

#buscamos una cadena en otra cadena, -1 si no lo encuentra
busuqueda_find = cadena2.find("o")

#buscamos una cadena en otra cadena, si no lo encuentra, lanza un error, exception
busqueda_index = cadena2.index("b")

#si es numerico devuelve True, sino False
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve True, sino False
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene la cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena esta dentro de otra cadena, devuelve True o False
empieza_con = cadena1.startswith("b")

termina_con = cadena1.endswith("la") 

#reemplazamos una cadena por otra
cadena_nueva = cadena1.replace("a","i")

#separa cadenas por las cadenas que pasemos 
cadena_separada = cadena1.split(",")

print(cadena_separada)