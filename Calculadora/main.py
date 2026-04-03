import sys
sys.path.append('d:\\Jenny\\Desktop\\Python\\multiplicacion_y_division')
sys.path.append('d:\\Jenny\\Desktop\\Python\\suma_y_resta')

import div as division 
import mult as multiplicaion
import resta1 as resta
import suma1 as suma

print(f'La division de dos numeros es: {division.division_dos_numeros(15,3)}')
print(f'La multiplicacion de dos numeros es: {multiplicaion.multi_dos_numeros(10,10)}')
print(f'La resta de dos nuemros es: {resta.restar_dos_numeros(10,5)}')
print(f'La suma de dos numeros es: {suma.suma_dos_numeros(7,7)}')