class Inscripcion:
    __fechaInscripcion= str
    __pago= bool
    __persona= object
    __taller= object
    
    def __init__(self,fecha,pago,persona,taller):
        self.__fechaInscripcion= fecha
        self.__pago= pago
        self.__persona= persona
        self.__taller= taller
        
    def getFechaInscripcion(self):
        return self.__fechaInscripcion    
        
    def getPago(self):
        return self.__pago    
        
    def getPersona(self):
        return self.__persona
    
    def getTaller(self):
        return self.__taller
    
    def updatePago(self):
        self.__pago= True
        print("Pago realizado con éxito!")