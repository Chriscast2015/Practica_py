#modulo en una carpeta de la misma ruta
#import funciones_buenas.saludar


import sys
sys.path.append('d:\\Jenny\\Desktop\\Python\\funciones_buenas')

import saludar as modulo_saludo

print(modulo_saludo.saludar("Xavi"))