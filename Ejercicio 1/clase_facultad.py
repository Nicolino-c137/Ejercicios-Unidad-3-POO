from manejador_carreras import Manejador_Carreras

class Facultad:
    __codigo= int
    __nombre= str
    __direccion= str
    __localidad= str
    __telefono= str
    __carreras= object
    
    def __init__(self,cod,nombre,direc,localidad,tel):
        self.__codigo= cod
        self.__nombre= nombre
        self.__direccion= direc
        self.__localidad= localidad
        self.__telefono= tel
        self.__carreras= Manejador_Carreras()
        
    def agregarCarrera(self,una_carrera):
        self.__carreras.agregarCarrera(una_carrera)
        
    def mostrarCarreras(self):
        self.__carreras.mostrarNombreyDuracion()
        
    def buscar(self,carrera):
        resultado, cod= self.__carreras.buscarCarrera(carrera)
        return resultado, cod
        
    def getLen(self):
        return len(self.__carreras)    
        
    def __str__(self):
        return f"{self.__codigo}, {self.__nombre}, {self.__direccion}, {self.__localidad}, {self.__telefono}"    
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono