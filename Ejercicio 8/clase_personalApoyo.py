from clase_personal import Personal

class PersonalApoyo(Personal):
    __categoria= int
    __categoriaA= 0.1
    __categoriaB= 0.2
    __categoriaC= 0.3
    
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
            porcentaje= self.__categoriaA * self.getSueldoBasico()
        elif self.getCategoria() >= 11 and self.getCategoria() <= 20:
            porcentaje= self.__categoriaB * self.getSueldoBasico()
        elif self.getCategoria() >= 21:
            porcentaje= self.__categoriaC * self.getSueldoBasico()
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
    
    @classmethod
    def modificarPorcentajeCategoria(cls,categoria,porcentaje):
        if 1 <= categoria <= 10:
            cls.__categoriaA= porcentaje
        elif 11 <= categoria <= 20:
            cls.__categoriaB= porcentaje
        elif categoria >= 21:
            cls.__categoriaC= porcentaje