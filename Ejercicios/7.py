#adivina numero

numero_secreto = 8

while True:
    numero = int(input("Ingrese número secreto: "))
    if numero != numero_secreto:
        print("Numero Incorrecto")
    else: 
        print(f"Numero {numero_secreto} es el numero secreto")
        break
    

    
        