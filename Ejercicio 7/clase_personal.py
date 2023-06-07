import abc
from abc import ABC

class Personal(ABC):
    __cuil= str
    __apellido= str
    __nombre= str
    __sueldoBasico= int
    __antiguedad= int
    
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,carreraDicta='',cargo='',catedra='',areaInvestigacion='',tipoDeInvestigacion=''):
        self.__cuil= cuil
        self.__apellido= apellido
        self.__nombre= nombre
        self.__sueldoBasico= sueldo
        self.__antiguedad= antiguedad
        
    def getCuil(self):
        return self.__cuil
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getAntiguedad(self):
        return self.__antiguedad  
    
    @abc.abstractclassmethod
    def getSueldo():
        pass    
    
    def mostrar(self):
        print(f"CUIL: {self.getCuil()}, Apellido: {self.getApellido()}, Nombre: {self.getNombre()}, Antiguedad: {self.getAntiguedad()}, Sueldo Básico: ${self.getSueldoBasico()}")  