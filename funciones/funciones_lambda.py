numeros = [1,2,3,4,5,6,7,8,9]

#funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2 


#funcion es par o no
#def es_par(num):
#   if (num%2==1):
#       return True
     
#funcion fliter
#numeros_pares = filter(es_par,numeros)


#funcion es par o no con lambda

numeros_pares = filter(lambda numero:numero%2==1,numeros )
print(list(numeros_pares))