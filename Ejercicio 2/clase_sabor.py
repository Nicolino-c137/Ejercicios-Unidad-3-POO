class Sabor:
    __idSabor= int
    __ingredientes= str
    __nombreSabor= str
    
    def __init__(self,id,ingredientes,nombre):
        self.__idSabor= id
        self.__ingredientes= ingredientes
        self.__nombreSabor= nombre
        
    def getIdSabor(self):
        return self.__idSabor
    
    def getNombreSabor(self):
        return self.__nombreSabor