#def frase (nombre, apellido, adjetivo):
 #   return f'{nombre} {apellido}, eres muy {adjetivo}'

#frase_resultante = frase(adjetivo="listo", apellido="Castro", nombre="Xavi")
#print(frase_resultante)

def frase (nombre, apellido, adjetivo="Tonto"):
    return f'{nombre} {apellido}, eres muy {adjetivo}'

frase_resultante = frase("Christian", "Castro", "Listo")
print(frase_resultante)