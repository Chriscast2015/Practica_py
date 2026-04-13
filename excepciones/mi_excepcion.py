#Creando una excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")
        
        
#Lanzando la excepcion
raise MiExcepcion("jajajajjajajjaj")

#manejando la excepcion
try:
    raise MiExcepcion("jajajajjajajjaj")
except:
    print("Como vas a cometer ese error")