class Persona:
    __nombre= str
    __direccion= str
    __dni= str
    
    def __init__(self,nombre,direcc,dni):
        self.__nombre= nombre
        self.__direccion= direcc
        self.__dni= dni
        
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getDni(self):
        return self.__dni