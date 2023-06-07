from clase_vehiculo import Vehiculo
from datetime import date

class Usado(Vehiculo):
    __patente= str
    __año= int
    __kms= int
    
    def __init__(self,marca,modelo,cantPuertas,color,precioBase,patente,ano,kilometraje):
        super().__init__(marca,modelo,cantPuertas,color,precioBase)
        self.__patente= patente
        self.__año= ano
        self.__kms= kilometraje
        
    def getMarca(self):
        return super().getMarca()
    
    def getModelo(self):
        return super().getModelo()
    
    def getCantPuertas(self):
        return super().getCantPuertas()
    
    def getColor(self):
        return super().getColor()
    
    def getPrecioBase(self):
        return super().getPrecioBase()
        
    def getPatente(self):
        return self.__patente
    
    def getAño(self):
        return self.__año
    
    def getKilometraje(self):
        return self.__kms
            
    def calcularAntiguedad(self):
        today= date.today()
        añoActual= today.year
        return añoActual - self.__año
        
    def calcularImporteVenta(self):
        precio= self.getPrecioBase()
        antiguedad= self.calcularAntiguedad()
        if self.__kms > 100000:
            importe= precio - (((1/100)*precio)*antiguedad) - ((2/100)*precio)
        else: importe= precio - (((1/100)*precio)*antiguedad)
        return importe
    
    def mostrarImporteVenta(self):
        importe= self.calcularImporteVenta()
        print(f"El precio del vehículo es de ${importe}")
        
    def mostrarDatos(self):
        super().mostrarVehiculo()
        print(f"""Patente: {self.getPatente()}  Año: {self.getAño()}
Kilometraje: {self.getKilometraje()}""")
    
    def setPrecioBase(self,nuevo_precio):
        super().setPrecioBase(nuevo_precio)
    
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca= self._Vehiculo__marca,
                modelo= self._Vehiculo__modelo,
                cantPuertas= self._Vehiculo__cantPuertas,
                color= self._Vehiculo__color,
                precioBase= self._Vehiculo__precioBase,
                patente= self.__patente,
                ano= self.__año,
                kilometraje= self.__kms
            )
        )
        return d