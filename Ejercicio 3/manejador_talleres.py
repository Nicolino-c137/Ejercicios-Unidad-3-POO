import numpy as np
from clase_taller_capacitacion import TallerCapacitacion

class ManejadorTalleres:
    __talleres= None
    
    def __init__(self,dimension):
        self.__talleres= np.empty(dimension,dtype=TallerCapacitacion)
        
    def agregarTaller(self,un_taller):
        id= un_taller.getIdTaller()
        self.__talleres[id-1]= un_taller
        
    def mostrarTalleresDisponibles(self):
        for i in range(len(self.__talleres)):
            print(f"{self.__talleres[i].getIdTaller()} {self.__talleres[i].getNombreTaller()}")
        
    def inscribirPersona(self,inscripto,taller):
        id= taller.getIdTaller()
        self.__talleres[id-1].addInscripto(inscripto)
        self.__talleres[id-1].updateVacantes()    
        
    def buscar_y_retornarTaller(self,id):
        i= 0
        bandera= False
        while not bandera and i < len(self.__talleres):
            if id == self.__talleres[i].getIdTaller():
                bandera= True
                taller= self.__talleres[i]
            i+= 1    
        return taller
        
    def verificarExistenciaTaller(self,id):
        i= 0
        bandera= False
        while not bandera and i < len(self.__talleres):
            if id == self.__talleres[i].getIdTaller():
                bandera= True
            i+= 1    
        return bandera
    
    def listarAlumnosInscriptos(self,id):
        self.__talleres[id-1].mostrarAlumnos()
        