from clase_investigador import Investigador
from clase_docente import Docente

class DocenteInvestigador(Docente,Investigador):
    __categoriaProgramaIncentivos= str
    __importeExtra= int
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carreraDicta,cargo,catedra,categoriaProgramaIncentivos,importeExtra,areaInvestigacion,tipoDeInvestigacion):
        super().__init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carreraDicta,cargo,catedra,areaInvestigacion,tipoDeInvestigacion)
        self.__categoriaProgramaIncentivos= categoriaProgramaIncentivos
        self.__importeExtra= importeExtra
        
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
        return super().getAreaInvestigacion()
    
    def getTipoInvestigacion(self):
        return super().getTipoInvestigacion()
    
    def getCargo(self):
        return super().getCargo()
    
    def getCarrera(self):
        return super().getCarrera()
    
    def getCatedra(self):
        return super().getCatedra()
    
    def getCategoriaProgramaIncentivos(self):
        return self.__categoriaProgramaIncentivos
    
    def getImporteExtra(self):
        return self.__importeExtra
    
    def getSueldo(self):
        sueldo= Docente.getSueldo() + self.getImporteExtra()
        return sueldo
    
    def mostrar(self):
        super().mostrar()
        print(f"Importe Extra: ${self.getImporteExtra()}, Categoría en el Programa de Incentivos de Investigación: {self.getCategoriaProgramaIncentivos()}")
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            atributos= dict(
                cuil= self._Personal__cuil,
                apellido= self._Personal__apellido,
                nombre= self._Personal__nombre,
                sueldoBasico= self._Personal__sueldoBasico,
                antiguedad= self._Personal__antiguedad,
                carreraDicta= self._Docente__carrera,
                cargo= self._Docente__cargo,
                catedra= self._Docente__catedra,
                areaInvestigacion= self._Investigador__areaInvestigacion,
                tipoDeInvestigacion= self._Investigador__tipoDeInvestigacion,
                categoriaProgramaIncentivos= self.__categoriaProgramaIncentivos,
                importeExtra= self.__importeExtra
            )
        )
        return d