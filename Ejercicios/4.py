contrasenia_db = str(123)
usuario_db = "xavi"

usuario = input("Ingrese su usuario: ")
contrasenia = input("Ingrese su contraseña: ")

if contrasenia == contrasenia_db and usuario_db == usuario:
    print("Ingresando correctamente")
    
else:
    print("Contraseña incorrecta")