from zope.interface import Interface

class ILista(Interface):
    def insertarElementoPosicionDeseada(elemento,posicion):
        pass
    
    def agregarElementoalFinal(elemento):
        pass
    
    def mostrarElemento(posicion):
        pass