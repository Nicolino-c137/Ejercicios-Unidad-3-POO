from clase_nodo import Nodo
from clase_docente import Docente
from clase_investigador import Investigador
from clase_personalApoyo import PersonalApoyo
from clase_personal import Personal
from clase_docente_investigador import DocenteInvestigador
from interfaz_lista import ILista
from zope.interface import implementer

@implementer (ILista)
class Coleccion():
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
     
    def agregarAgente(self,agente):
        nodo= Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo= nodo
        self.__actual= nodo
        self.__tope+= 1
        
    """Método de la interface ILista"""  
    def agregarElementoAlFinal(self,agente):
        if self.__comienzo is None:
            #si la lista esta vacia, el elemento se agrega al comienzo
            self.agregarAgente(agente)
        else:
            #sino al final
            nuevo_nodo= Nodo(agente)
            for nodo in self:
                if nodo.getSiguiente() is None:
                    nodo.setSiguiente(nuevo_nodo)
            self.__tope+= 1
            print("Operación exitosa!")

            
    """Método de la interface ILista"""
    def insertarElementoPosicionDeseada(self,agente,posicion):
        if posicion == 1:
            self.agregarAgente(agente)
        else:
            assert posicion <= self.__tope, f"La posición ingresada debe ser menor o igual a {self.__tope}"
            nuevo_nodo= Nodo(agente)
            for nodo in self:
                if self.__index == posicion-1:
                    nuevo_nodo.setSiguiente(nodo.getSiguiente())
                    nodo.setSiguiente(nuevo_nodo)
            self.__tope+= 1  
        print("Operación exitosa!")
            
    """Método de la interface ILista"""
    def mostrarElemento(self,posicion):
        assert posicion <= self.__tope, f"La posición ingresada debe ser menor o igual a {self.__tope}"
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            if self.__index == posicion:
                print(type(nodo.getDato()))
                bandera= True
        self.__actual= self.__comienzo
        
    def verificarExistenciaCarrera(self,carrera):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            agente= nodo.getDato()
            if isinstance(agente,Docente):
                if carrera == agente.getCarrera():
                    bandera= True
        self.__actual= self.__comienzo
        return bandera
    
    def ordenarPorNombre(self,carrera):
        lista= []
        for nodo in self:
            agente= nodo.getDato()
            if isinstance(agente,DocenteInvestigador):
                if agente.getCarrera() == carrera:
                    lista.append(agente)
        lista= sorted(lista,key=lambda docente: docente.getNombre())
        self.listarDocentesInvestigadores(lista)
    
    def ordenarPorApellido(self):
        lista= []
        for nodo in self:
            agente= nodo.getDato()
            lista.append(agente)
        lista= sorted(lista,key=lambda personal: personal.getApellido())
        self.listarPersonal(lista)
    
    def listarPersonal(self,lista):
        print("Nombre, Apellido, Tipo de Agente, Sueldo")
        print("---------------------------------------------")
        for i in range(len(lista)):
            print(f"{lista[i].getNombre()}, {lista[i].getApellido()}, {type(lista[i])}, ${lista[i].getSueldo()}")
    
    def listarDocentesInvestigadores(self,lista):
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(len(lista)):
            print(f"{lista[i].mostrar()}")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            
    def verificarExistenciaArea(self,area):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            personal= nodo.getDato()
            if isinstance(personal,Investigador):
                if personal.getAreaInvestigacion() == area:
                    bandera= True
        self.__actual= self.__comienzo
        return bandera
     
    def mostrarCantidadPersonalSegunAreaInvestigacion(self,area):
        cantProfInv= 0
        cantInv= 0
        for nodo in self:
            pass
        for nodo in self:
            personal= nodo.getDato()
            if isinstance(personal,DocenteInvestigador):
                cantProfInv+= 1
            if isinstance(personal,Investigador) and personal.getAreaInvestigacion() == area:
                cantInv+= 1
        print(f"Hay {cantProfInv} Docentes Investigadores")
        print(f"{cantInv} Investigador/es trabajan en el área de {area}")
    
    def verificarExistenciaCategoria(self,categoria):
        bandera= False
        while not bandera and self.__index < self.__tope:
            nodo= self.__next__()
            personal= nodo.getDato()
            if isinstance(personal,DocenteInvestigador):
                if personal.getCategoriaProgramaIncentivos() == categoria:
                    bandera= True
        self.__actual= self.__comienzo
        return bandera
    
    def listarDocentesInvestigadoresSegunCategoria(self,categoria):
        acum= 0
        print("Apellido, Nombre, Importe Extra")
        print("--------------------------------------")
        for nodo in self:
            personal= nodo.getDato()
            if isinstance(personal,DocenteInvestigador):
                if personal.getCategoriaProgramaIncentivos() == categoria:
                    acum+= personal.getImporteExtra()
                    print(f"{personal.getApellido()}, {personal.getNombre()}, {personal.getImporteExtra()}")
        print("--------------------------------------")
        print(f"La Secretaría de Investigación debe solicitar al Ministerio un importe de ${acum}")   
        
    def toJSON(self):
        d= dict(
            __class__= self.__class__.__name__,
            nodos= [nodo.toJSON() for nodo in self]
        )
        return d