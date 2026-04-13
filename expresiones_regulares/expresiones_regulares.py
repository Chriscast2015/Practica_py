import re

texto = '''hola. como Estas? cadena 1 .
esta es la linea 258 de texto.
esta es la linea final(linea 3 )'''

#Haciendo una busqueda simple 
#resultado = re.findall("esta",texto)

#\D --busca TODO menos digitos numericos del 0 al 9
#resultado = re.findall(r"\D",texto)

#\w --busca caracteres alfanumericos, es decir letras mayusculas y minusculas, guion bajo y numeros del 0 al 9
#resultado = re.findall(r"\w",texto)

#\W --busca todo MENOS caracteres alfanumericos, es decir letras mayusculas y minusculas, guion bajo y numeros del 0 al 9
#resultado = re.findall(r"\W",texto)

#\s --busca espacios en blanco -> espacios, tabuladores, saltos de linea
#resultado = re.findall(r"\s",texto)

#\S --busca TODO menos espacios en blanco -> espacios, tabuladores, saltos de linea
#resultado = re.findall(r"\S",texto)

#. --busca TODO menos saltos de linea
#resultado = re.findall(r'.',texto)

#. --busca saltos de linea
#resultado = re.findall(r'\n',texto)

#\ -- cancelar caracteres especiales, cancelar la funcion del punto y busca puntos 
#resultado = re.findall(r'\.',texto)

#Armando una cadena que busque un numero seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s",texto)

#^ -- busca el inicio de una linea
#flags=re.M -- activa la multilinea 
#resultado = re.findall(r"^esta",texto,flags=re.M)

#$ -- busca el final de una linea 
#resultado = re.findall(r"1$",texto,flags=re.M)

#{n} -> busca n cantidad de veces el calor de la izquierda
#resultado = re.findall(r"\d{3}\s", texto)

#{n,m} -> al menos n, como maximo m
#resultado = re.findall(r"\d{1,4}\s", texto)

#| -> busca una cosa u otra
resultado = re.findall(r"\d{1,4}|hola", texto)

print(resultado)
