from clase_sabor import Sabor
import csv

class ManejaSabores:
    __listaSabores= list
    __contSaborPedido= list
    
    def __init__(self):
        self.__listaSabores= []
        self.__contSaborPedido= []
        
    def addSabor(self,un_sabor):
        self.__listaSabores.append(un_sabor)   
        self.__contSaborPedido.append(0) 
        
    def lecturaArchivo(self):
        with open ("sabores.csv",encoding="utf8") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            for fila in reader:
                idSabor= int(fila[0])
                ingredientes= fila[1]
                nombreSabor= fila[2]
                un_sabor= Sabor(idSabor,ingredientes,nombreSabor)
                self.addSabor(un_sabor)
                
    def mostrarSaboresDisponibles(self):
        for i in range(len(self.__listaSabores)):
            print(f"{self.__listaSabores[i].getIdSabor()} {self.__listaSabores[i].getNombreSabor()}")
           
    def getSabor(self,id):
        i= 0
        bandera= False
        while not bandera and i < len(self.__listaSabores):
            if self.__listaSabores[i].getIdSabor() == id:
                sabor= self.__listaSabores[i]
                bandera= True
            i+= 1
        return sabor      
    
    def cerearContador(self):
        for i in range(len(self.__contSaborPedido)):
            self.__contSaborPedido[i]= 0
            
    def mostrarCont(self):
        for i in range(len(self.__contSaborPedido)):
            if self.__contSaborPedido[i] > 0:
                print(f"{self.getNombreSaborsegunId(i+1)}")
    
    def incrementarContador(self,id):
        self.__contSaborPedido[id]+= 1
      
    def calcularMayor(self):
        max= -11111  
        for i in range(len(self.__contSaborPedido)):
            if self.__contSaborPedido[i] > max:
                max= self.__contSaborPedido[i]
                k= i
        self.__contSaborPedido[k]= 0  #se pone en 0 el maximo encontrado para que en cada iteracion no se repita el maximo
        return k+1
        
    def calcularTop5Sabores(self):
        lista5Sabores= []
        for i in range(5):
            id= self.calcularMayor()
            lista5Sabores.append(id)
        return lista5Sabores
            
    def mostrarSabores(self,sabores):
        for i in range(len(sabores)):
            nombre= self.getNombreSaborsegunId(sabores[i])
            print(f"{nombre}")
            
    def getNombreSaborsegunId(self,id):
        i= 0
        bandera= False
        while not bandera and i < len(self.__listaSabores):
            if self.__listaSabores[i].getIdSabor() == id:
                nombre= self.__listaSabores[i].getNombreSabor()
                bandera= True
            i+= 1
        return nombre