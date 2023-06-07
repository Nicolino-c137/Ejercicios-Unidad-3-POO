class TallerCapacitacion:
    __idTaller= int
    __nombre= str
    __vacantes= int
    __montoInscripcion= int
    __inscriptos= list
    
    def __init__(self,id,nombre,vacantes,monto):
        self.__idTaller= id
        self.__nombre= nombre
        self.__vacantes= vacantes
        self.__montoInscripcion= monto
        self.__inscriptos= []
        
    def getIdTaller(self):
        return self.__idTaller
    
    def getNombreTaller(self):
        return self.__nombre
    
    def getMonto(self):
        return self.__montoInscripcion
    
    def updateVacantes(self):
        if self.__vacantes != 0:
            self.__vacantes-= 1
        else: print("No hay mas vacantes disponibles")
        
    def addInscripto(self,un_inscripto):
        self.__inscriptos.append(un_inscripto)
        
    def mostrarAlumnos(self):
        for i in range(len(self.__inscriptos)):
            persona= self.__inscriptos[i].getPersona()
            print(f"DNI: {persona.getDni()}, Nombre: {persona.getNombre()}, Dirección: {persona.getDireccion()}")