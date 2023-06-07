from clase_vehiculo import Vehiculo

class Nuevo(Vehiculo):
    __version= str
    
    def __init__(self,marca,modelo,cantPuertas,color,precioBase,version):
        super().__init__(marca,modelo,cantPuertas,color,precioBase)
        self.__version= version
       
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
        
    def getVersion(self):
        return self.__version
        
    def calcularImporteVenta(self):
        precio= self.getPrecioBase()
        if self.__version == "Full":
            importe= precio + ((10/100)*precio) + ((2/100)*precio)
        else: importe= precio + ((10/100)*precio)
        return importe
    
    def mostrarImporteVenta(self):
        importe= self.calcularImporteVenta()
        print(f"El precio del vehículo es de ${importe}")
    
    def mostrarDatos(self):
        super().mostrarVehiculo()
        print(f"Versión: {self.getVersion()}")
    
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca= self._Vehiculo__marca,
                modelo= self._Vehiculo__modelo,
                cantPuertas= self._Vehiculo__cantPuertas,
                color= self._Vehiculo__color,
                precioBase= self._Vehiculo__precioBase,
                version= self.__version   
            )
        )
        return d