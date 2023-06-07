from clase_personal import Personal

class PersonalApoyo(Personal):
    __categoria= int
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__categoria= categoria
        
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
    
    def getCategoria(self):
        return self.__categoria
    
    def calcularPorcentajePorAntiguedad(self):
        porcentaje= self.getSueldoBasico() + ((self.getAntiguedad()/100) * self.getSueldoBasico())
        return porcentaje
    
    def calcularPorcentajePorCategoria(self):
        if self.getCategoria() >= 1 and self.getCategoria() <= 10:
            porcentaje= (10/100) * self.getSueldoBasico()
        elif self.getCategoria() >= 11 and self.getCategoria() <= 20:
            porcentaje= (20/100) * self.getSueldoBasico()
        elif self.getCategoria() >= 21:
            porcentaje= (30/100) * self.getSueldoBasico()
        return porcentaje
    
    def getSueldo(self):
        sueldo= self.getSueldoBasico() + self.calcularPorcentajePorAntiguedad() + self.calcularPorcentajePorCategoria()
        return sueldo
    
    def mostrar(self):
        super().mostrar()
        print(f"Categoría: {self.getCategoria()}")
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            atributos= dict(
                cuil= self._Personal__cuil,
                apellido= self._Personal__apellido,
                nombre= self._Personal__nombre,
                sueldoBasico= self._Personal__sueldoBasico,
                antiguedad= self._Personal__antiguedad,
                categoria= self.__categoria
            )
        )
        return d