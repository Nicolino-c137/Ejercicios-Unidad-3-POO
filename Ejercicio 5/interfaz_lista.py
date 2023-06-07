from zope.interface import Interface

class ILista(Interface):
    def insertarElemento(elemento,posicion):
        pass
    
    def agregarElementoalFinal(elemento):
        pass
    
    def mostrarElemento(posicion):
        pass