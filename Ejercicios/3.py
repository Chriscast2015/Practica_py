edad = int(input("Ingrese su edad:"))

if edad <= 17:
    print("Es menor de edad")
    
elif edad >= 18 and edad <=64:
    print("Es mayor de edad")

elif edad >= 65:
    print("Es adulto mayor")   