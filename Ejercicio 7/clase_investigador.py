from clase_personal import Personal

class Investigador(Personal):
    __areaInvestigacion= str
    __tipoDeInvestigacion= str
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoDeInvestigacion,carreraDicta='',cargo='',catedra=''):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoDeInvestigacion,carreraDicta,cargo,catedra)
        self.__areaInvestigacion= areaInvestigacion
        self.__tipoDeInvestigacion= tipoDeInvestigacion
        
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
    
    def getAreaInvestigacion(self):
        return self.__areaInvestigacion
    
    def getTipoInvestigacion(self):
        return self.__tipoDeInvestigacion
    
    def calcularPorcentajePorAntiguedad(self):
        porcentaje= self.getSueldoBasico() + ((self.getAntiguedad()/100) * self.getSueldoBasico())
        return porcentaje
    
    def getSueldo(self):
        sueldo= self.getSueldoBasico() + self.calcularPorcentajePorAntiguedad()
        return sueldo
    
    def mostrar(self):
        super().mostrar()
        print(f"Area de Investigacion: {self.getAreaInvestigacion()}, Tipo de Investigación: {self.getTipoInvestigacion()}")
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            atributos= dict(
                cuil= self._Personal__cuil,
                apellido= self._Personal__apellido,
                nombre= self._Personal__nombre,
                sueldoBasico= self._Personal__sueldoBasico,
                antiguedad= self._Personal__antiguedad,
                areaInvestigacion= self.__areaInvestigacion,
                tipoDeInvestigacion= self.__tipoDeInvestigacion
            )
        )
        return d