#multipicación de números
def calcular_multiplicacion():
    multiplicacion = 1

    while True:
        numero = int(input("Ingrese un numero: "))
        if numero == 0:
            break

        multiplicacion *= numero
        
    return multiplicacion


#Tabla de multiplicar 

def tabla_multiplicar():
    numero = int(input("Ingrese un número de la tabla de multiplicar: "))

    for i in range (1,11,):
        print(numero, "x",i,"=",numero*i)


resultado = tabla_multiplicar()
print(f"resultado: {resultado}")    

