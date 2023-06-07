class Helado:
    __peso= float
    __precio= float
    __sabores= list
    
    def __init__(self,peso,precio,sabor=None):
        self.__peso= peso
        self.__precio= precio
        if sabor != None:
            self.__sabores= []
            self.addSabor(sabor)            
        
    def addSabor(self,sabor):
        self.__sabores.append(sabor) 
        
    def getPeso(self):
        return self.__peso
    
    def getPrecio(self):
        return self.__precio
    
    def getSabores(self):
        return self.__sabores