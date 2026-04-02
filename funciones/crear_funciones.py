#creando una funcion simple 
#def saludar():
 #   print("Holi, mi nombre es Chris")
    
#Ejecutando la funcion simple 
#saludar()

#Función con parametros
def saludar(nombre,sexo):
    sexo =sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "crack"
    

    print(f'Hola {adjetivo}, mi nombre es: {nombre}')
    
    
saludar("Chris","mu")
saludar("Chris","hoMbre")

#funcion que nos retorne valores 
def crear_contraseña(num):
    chars = 'abcdefghij'
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num -2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" 
    return(contraseña)

crear_contraseña(52)