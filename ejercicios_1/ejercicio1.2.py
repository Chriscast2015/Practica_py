frase = input ("Dime una frase y te calculo cuanto tardarías se tubieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
    print("Esa frase es muy larga, no la voy a decir")
    
else:

    print(f'dijiste {cantidad_de_palabras} palabras, tardarias {cantidad_de_palabras/2} segundos en decirla')
    print(f'Dalto lo diría en {cantidad_de_palabras/2*1.3} segundos en decirlo')

