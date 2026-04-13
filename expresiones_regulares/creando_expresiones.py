import re

#Detectando un numero CABA y ocultarlo 
texto = "Hola Pedro, mi numero es: +593 83 946-002"

pattern = r'\+\d{1,3}\s\d{1,2}\s\d{1,3}-\d{3}'

reemplazo = re.sub(pattern,"(Número oculto)",texto)

print(reemplazo)