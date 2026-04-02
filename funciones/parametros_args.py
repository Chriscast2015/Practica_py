#def suma(a,b):
 #   return a + b 
#resultado = suma(5,3)


#forma optima de sumar valores 
def suma_total(numeros):
    return sum([*numeros])

resultado2= suma_total([10,5,15,5,20])



#parametro args *

def suma(nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma("Xavi",5,15,5,20)
print(resultado)