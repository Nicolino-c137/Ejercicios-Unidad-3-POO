from clase_personal import Personal

class Docente(Personal):
    __carrera= str
    __cargo= str
    __catedra= str
    __simple= 0.1
    __semiexclusivo= 0.2
    __exclusivo= 0.5
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carreraDicta,cargo,catedra,areaInvestigacion='',tipoDeInvestigacion=''):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carreraDicta,cargo,catedra,areaInvestigacion,tipoDeInvestigacion)
        self.__carrera= carreraDicta
        self.__cargo= cargo
        self.__catedra= catedra
        
    def getCuil(self):
        return super().getCuil()
    
    def getApellido(self):
        return super().getApellido()
    
    def getNombre(self):
        return super().getNombre()
    
    def getSueldoBasico(self):
        return super().getSueldoBasico()
    
    def getAntiguedad(self):
        return super().getAntiguedad()
    
    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def calcularPorcentajePorAntiguedad(self):
        porcentaje= self.getSueldoBasico() + ((self.getAntiguedad()/100) * self.getSueldoBasico())
        return porcentaje
    
    def calcularPorcentajePorCargo(self):
        if self.getCargo() == "Simple":
            porcentaje= self.__simple * self.getSueldoBasico()
        elif self.getCargo() == "Semiexclusivo":
            porcentaje= self.__semiexclusivo * self.getSueldoBasico()
        elif self.getCargo() == "Exclusivo":
            porcentaje= self.__exclusivo * self.getSueldoBasico()
        return porcentaje
    
    def getSueldo(self):
        sueldo= self.getSueldoBasico() + self.calcularPorcentajePorAntiguedad() + self.calcularPorcentajePorCargo()
        return sueldo
    
    def mostrar(self):
        super().mostrar()
        print(f"Cargo: {self.getCargo()}, Carrera en la que dicta clases: {self.getCarrera()}, Cátedra: {self.getCatedra()}")
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            atributos= dict(
                cuil= self._Personal__cuil,
                apellido= self._Personal__apellido,
                nombre= self._Personal__nombre,
                sueldoBasico= self._Personal__sueldoBasico,
                antiguedad= self._Personal__antiguedad,
                carreraDicta= self.__carrera,
                cargo= self.__cargo,
                catedra= self.__catedra
            )
        )
        return d
    
    @classmethod
    def modificarPorcentajeCargo(cls,cargo,porcentaje):
        if cargo == "Simple":
            cls.__simple= porcentaje
        elif cargo == "Semiexclusivo":
            cls.__semiexclusivo= porcentaje
        elif cargo == "Exclusivo":
            cls.__exclusivo= porcentaje