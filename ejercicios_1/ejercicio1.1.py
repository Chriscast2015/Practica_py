#promedio duracion otros cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
#curso dalto
dalto_curso = 1.5 

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5




#Diferencias de duracion 
diferencia_con_min = 100 - dalto_curso/otros_cursos_min * 100 
diferencia_con_max = 100 - dalto_curso/otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso/otros_cursos_promedio * 100 

resultado_max = round(diferencia_con_max,2)

#Diferencia de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio/crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso *1000//crudo_dalto / 10 

#Ejercicio A
print("Ejercicio A")
print(f'El curso de dalto dura: {diferencia_con_min}% menos que más rapido')
print(f'El curso de dalto dura: {resultado_max}% menos que más lento')
print(f'El curso de dalto dura: {diferencia_con_promedio}% menos que el promedio')
print("-------------------")

#Ejercicio B
print("Ejercicio B")
print(f'Un curso promedio elimina un: {tiempo_vacio_promedio}% de tiempo vacío')
print(f'Este curso eliminó un: {tiempo_vacio_dalto}% de tiempo vacío')
print("-------------------")
#Mostrando diferencias si los cursos duraran 10 horas
print("Ejercicio ") 
print(f'Ver 10 horas de este curso es equivalente a ver {otros_cursos_promedio * 100 //dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos es equivalente a ver {dalto_curso * 100 //otros_cursos_promedio / 10} horas de este curso')