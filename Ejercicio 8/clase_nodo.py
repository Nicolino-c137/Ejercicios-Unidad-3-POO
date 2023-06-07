from clase_personal import Personal

class Nodo:
    __dato= Personal
    __siguiente= object
    
    def __init__(self,dato=None):
        self.__dato= dato
        self.__siguiente= None
        
    def setSiguiente(self,siguiente):
        self.__siguiente= siguiente
        
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__dato
    
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            __atributos= dict(
                agente= self.__dato.toJSON()
            )
        )  
        return d          