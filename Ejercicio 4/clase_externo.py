from clase_empleado import Empleado

class Externo(Empleado):
    __tarea= str
    __fechaInicio= str
    __fechaFinalizacion= str
    __montoViatico= int
    __costoObra= int
    __montoSeguroVida= int
    
    def __init__(self,dni,nombre,direccion,telefono,tarea,fechaI,fechaF,montoV,costo,montoS):
        super().__init__(dni,nombre,direccion,telefono)
        self.__tarea= tarea
        self.__fechaInicio= fechaI
        self.__fechaFinalizacion= fechaF
        self.__montoViatico= int(montoV)
        self.__costoObra= int(costo)
        self.__montoSeguroVida= int(montoS)
        
    def getDni(self):
        return super().getDni()
    
    def getNombre(self):
        return super().getNombre()
    
    def getDireccion(self):
        return super().getDireccion()
    
    def getTelefono(self):
        return super().getTelefono()
    
    def getTarea(self):
        return self.__tarea
    
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    
    def getCostoObra(self):
        return self.__costoObra
    
    def calcularSueldo(self):
        sueldo= self.__costoObra - self.__montoViatico - self.__montoSeguroVida
        return sueldo