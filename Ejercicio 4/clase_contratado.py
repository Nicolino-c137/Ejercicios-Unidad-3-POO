from clase_empleado import Empleado

class Contratado(Empleado):
    __fechaInicioContrato= str
    __fechaFinalizacionContrato= str
    __horasTrabajadas= int
    __valorXHora= int
     
    def __init__(self,dni,nombre,direccion,telefono,fechaI,fechaF,horas,valor):
        super().__init__(dni,nombre,direccion,telefono)
        self.__fechaInicioContrato= fechaI
        self.__fechaFinalizacionContrato= fechaF
        self.__horasTrabajadas= int(horas)
        self.__valorXHora= int(valor)
        
    def getDni(self):
        return super().getDni()
    
    def getNombre(self):
        return super().getNombre()
    
    def getDireccion(self):
        return super().getDireccion()
    
    def getTelefono(self):
        return super().getTelefono()
    
    def updateHorasTrabajadas(self,horas):
        self.__horasTrabajadas+= horas
        print("Operación éxitosa!")
        
    def calcularSueldo(self):
        sueldo= self.__horasTrabajadas * self.__valorXHora
        return sueldo