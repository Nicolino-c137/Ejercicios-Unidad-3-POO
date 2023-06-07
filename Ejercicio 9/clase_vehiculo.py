from abc import ABC
import abc

class Vehiculo(ABC):
    __marca= str
    __modelo= str
    __cantPuertas= int
    __color= str
    __precioBase= int
    
    def __init__(self,marca,modelo,cantPuertas,color,precio):
        self.__marca= marca
        self.__modelo= modelo
        self.__cantPuertas= cantPuertas
        self.__color= color
        self.__precioBase= precio
        
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getCantPuertas(self):
        return self.__cantPuertas
    
    def getColor(self):
        return self.__color    
        
    def getPrecioBase(self):
        return self.__precioBase
    
    def setPrecioBase(self,nuevo_precio):
        self.__precioBase= nuevo_precio
    
    @abc.abstractmethod
    def calcularImporteVenta():
        pass
    
    def mostrarVehiculo(self):
        print(f"""
Marca y modelo: {self.getMarca()}, {self.getModelo()}
Color: {self.getColor()}  Cant.Puertas: {self.getCantPuertas()}
Precio Base: ${self.getPrecioBase()}""")
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca= self.__marca,
                modelo= self.__modelo,
                cantPuertas= self.__cantPuertas,
                color= self.__color,
                precioBase= self.__precioBase     
            )
        )
        return d