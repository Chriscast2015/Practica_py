#2 listas, una con nombres y otra con apellidos 
nombres = ["Jose", "Josefina", "Andrea", "Isabella", "Mateo"]
apellidos = ["Castro","Dalto","De Luca", "Gray","Soto"]

#registrar esta información de forma optima

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido:{a}\n---------\n") for n,a in zip(nombres,apellidos)]
    