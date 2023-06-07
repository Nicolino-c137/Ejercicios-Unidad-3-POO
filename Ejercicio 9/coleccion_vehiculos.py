from clase_nodo import Nodo
from clase_nuevo import Nuevo
from clase_usado import Usado
from interfaz_lista import ILista
from zope.interface import implementer

@implementer(ILista)
class ColeccionVehiculos:
    __comienzo= Nodo
    __actual= Nodo
    __index= int
    __tope= int
    
    def __init__(self):
        self.__comienzo= None
        self.__actual= None
        self.__index= 0
        self.__tope= 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index == self.__tope:
            self.__actual= self.__comienzo
            self.__index= 0
            raise StopIteration
        else: 
            self.__index+= 1
            nodo= self.__actual
            self.__actual= self.__actual.getSiguiente()
            return nodo  
        
    def agregarVehiculo(self,un_vehiculo):
        nodo= Nodo(un_vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo= nodo
        self.__actual= nodo
        self.__tope+= 1
      
    """Método de la interface ILista"""  
    def agregarElementoalFinal(self,un_vehiculo):
        if self.__comienzo is None:
            #si la lista esta vacia, el elemento se agrega al comienzo
            self.agregarVehiculo(un_vehiculo)
        else:
            #sino al final
            nuevo_nodo= Nodo(un_vehiculo)
            for nodo in self:
                if nodo.getSiguiente() is None:
                    nodo.setSiguiente(nuevo_nodo)
            self.__tope+= 1
        
    """Método de la interface ILista"""
    def insertarElementoPosicionDeseada(self,un_vehiculo,posicion):
        if posicion == 1:
            self.agregarVehiculo(un_vehiculo)
        else:
            assert posicion <= self.__tope, f"La posición ingresada debe ser menor o igual a {self.__tope}"
            nuevo_nodo= Nodo(un_vehiculo)
            for nodo in self:
                if self.__index == posicion-1:
                    nuevo_nodo.setSiguiente(nodo.getSiguiente())
                    nodo.setSiguiente(nuevo_nodo)
            self.__tope+= 1     
            
    """Método de la interface ILista"""
    def mostrarElemento(self,posicion):
        assert posicion <= self.__tope, f"La posición ingresada debe ser menor o igual a {self.__tope}"
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            if self.__index == posicion-1:
                print(type(nodo.getVehiculo()))
                bandera= True
        self.__actual= self.__comienzo
        
    def getModelos(self):
        modelos= []
        for nodo in self:
            auto= nodo.getVehiculo()
            modelos.append(auto.getModelo())
        return modelos
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            nodos= [nodo.toJSON() for nodo in self]
        )
        return d
    
    def verificarExistenciaPatente(self,patente):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            vehiculo= nodo.getVehiculo()
            if isinstance(vehiculo,Usado):
                if vehiculo.getPatente() == patente:
                    bandera= True
        self.__actual= self.__comienzo
        return bandera
    
    def modificarPrecioBase_segunPatenteIngresada(self,patente,nuevo_precio):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            vehiculo= nodo.getVehiculo()
            if isinstance(vehiculo,Usado):
                if vehiculo.getPatente() == patente:
                    bandera= True
                    vehiculo.setPrecioBase(nuevo_precio)
                    print("Precio modificado con éxito!")
        self.__actual= self.__comienzo
        
    def getModeloSegunPosicion(self,posicion):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            if self.__index == posicion-1:
                vehiculo= nodo.getVehiculo()
                modelo= vehiculo.getModelo()
                bandera= True
        self.__actual= self.__comienzo
        return modelo
        
    def getImporteVentaSegunPatente(self,patente):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            vehiculo= nodo.getVehiculo()
            if isinstance(vehiculo,Usado):
                if vehiculo.getPatente() == patente:
                    bandera= True
                    importe= vehiculo.calcularImporteVenta()
        self.__actual= self.__comienzo
        return importe
            
    def mostrarPrecioVenta_segunPatenteIngresada(self,patente):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            vehiculo= nodo.getVehiculo()
            if isinstance(vehiculo,Usado):
                if vehiculo.getPatente() == patente:
                    bandera= True
                    importe= vehiculo.calcularImporteVenta()
        print(f"El precio del vehículo es de ${importe}")
        self.__actual= self.__comienzo
        
    def mostrarDatosVehiculo_segunImporte(self,importe):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            vehiculo= nodo.getVehiculo()
            if vehiculo.calcularImporteVenta() == importe:
                bandera= True
                vehiculo.mostrarDatos()
                vehiculo.mostrarImporteVenta()
        self.__actual= self.__comienzo    
        
    def buscarVehiculoEconomico(self):
        min= 999999999999
        for nodo in self:
            vehiculo= nodo.getVehiculo()
            if vehiculo.calcularImporteVenta() < min:
                min= vehiculo.calcularImporteVenta()
        return min
    
    def mostrarTodoslosVehiculosDisponibles(self):
        for nodo in self:
            vehiculo= nodo.getVehiculo()
            print(f"""
Modelo: {vehiculo.getModelo()}
Cantidad de puertas: {vehiculo.getCantPuertas()}""")
            vehiculo.mostrarImporteVenta()