from clase_empleado import Empleado

class Planta(Empleado):
    __sueldoBasico= int
    __antiguedad= int
    
    def __init__(self,dni,nombre,direccion,telefono,sueldo,antiguedad):
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldoBasico= int(sueldo)
        self.__antiguedad= int(antiguedad)
        
    def getDni(self):
        return super().getDni()
    
    def getNombre(self):
        return super().getNombre()
    
    def getDireccion(self):
        return super().getDireccion()
    
    def getTelefono(self):
        return super().getTelefono()
    
    def calcularSueldo(self):
        sueldo= self.__sueldoBasico + ((1/100)*self.__sueldoBasico) * self.__antiguedad
        return sueldo