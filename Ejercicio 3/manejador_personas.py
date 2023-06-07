from clase_persona import Persona

class ManejadorPersonas:
    __listaPersonas= list
    
    def __init__(self):
        self.__listaPersonas= []
        
    def cargarDatosPersona(self):
        dni= input("Ingrese el dni de la persona: ")
        nombre= input("Ingrese el nombre: ")
        direccion= input("Ingrese su domicilio: ")
        una_Persona= Persona(nombre,direccion,dni)
        self.addPersona(una_Persona)
        return una_Persona
        
    def addPersona(self,una_persona):
        self.__listaPersonas.append(una_persona)