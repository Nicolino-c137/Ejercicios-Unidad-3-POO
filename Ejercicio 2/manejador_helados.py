from clase_helado import Helado

class ManejaHelados:
    __listaHelados= list
    
    def __init__(self):
        self.__listaHelados= []
        
    def addVenta(self,un_helado):
        self.__listaHelados.append(un_helado)    
        
    def registrarVenta(self,gramos,sabor,cantSabores,m_S):
        precio= self.calcularPrecio(gramos)
        un_helado= Helado(gramos,precio,sabor)
        if cantSabores > 1:
            for i in range(cantSabores-1):
                id= int(input("Elija el sabor que desea: "))
                m_S.incrementarContador(id-1)
                sabor= m_S.getSabor(id)
                un_helado.addSabor(sabor)
        self.addVenta(un_helado)
        
    def calcularPrecio(self,gramos):
        if gramos == 1000:
            precio= 3300
        elif gramos == 500:
            precio= 1650
        elif gramos == 250:
            precio= 825
        elif gramos == 150:
            precio= 550
        elif gramos == 100:
            precio= 330
        return precio
    
    def calcularTotalGramos(self,gr,cant):
        retorna= gr/cant
        return retorna
    
    def calcularGramos(self,id):
        acum= 0
        for i in range(len(self.__listaHelados)):
            sabores= self.__listaHelados[i].getSabores()
            for j in range(len(sabores)):
                if sabores[j].getIdSabor() == id:
                    peso= self.__listaHelados[i].getPeso()
                    acum+= self.calcularTotalGramos(peso,len(sabores))
        return acum
    
    def getSabores_segunTipo(self,peso,m_S):
        m_S.cerearContador()
        for i in range(len(self.__listaHelados)):
            if self.__listaHelados[i].getPeso() == peso:
                sabores= self.__listaHelados[i].getSabores()
                for j in range(len(sabores)):
                    m_S.incrementarContador(sabores[j].getIdSabor()-1)
        
    def calcularImporteTotal(self):
        acum100= 0 
        acum150= 0
        acum250= 0
        acum500= 0
        acum1000= 0
        for i in range(len(self.__listaHelados)):
            if self.__listaHelados[i].getPeso() == 100:
                acum100+= self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getPeso() == 150:
                acum150+= self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getPeso() == 250:
                acum250+= self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getPeso() == 500:
                acum500+= self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getPeso() == 1000:
                acum1000+= self.__listaHelados[i].getPrecio()
        return acum100, acum150, acum250, acum500, acum1000