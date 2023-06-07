from clase_vehiculo import Vehiculo

class Nodo:
    __vehiculo= Vehiculo
    __siguiente= object
    
    def __init__(self,vehiculo=None):
        self.__vehiculo= vehiculo
        self.__siguiente= None
        
    def __str__(self):
        cadena= f"vehiculo= {self.__vehiculo}\n siguiente= {self.__siguiente}"
        return cadena
        
    def setSiguiente(self,siguiente):
        self.__siguiente= siguiente
        
    def getSiguiente(self):
        return self.__siguiente
        
    def getVehiculo(self):
        return self.__vehiculo
    
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                vehiculo= self.__vehiculo.toJSON()                    
            )
        )
        return d