#creando funcion que suma dos numeros 
def sumar_dos ():
    #Iniciando un bucle 
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertir a enteros y sumarlo 
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos 
        except Exception as e:
            print("te pedí un numero")
            print(f"ERROR: {e}")
        #si todo salio bine se termina el bucle 
        else:
            break 
        finally:
            print("Esto se ejecuta siempre")
    #mostrando el resultado    
    return resultado

print(sumar_dos())



