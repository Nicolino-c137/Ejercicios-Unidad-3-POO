import numpy as np
import csv
from clase_inscripcion import Inscripcion

class ManejadorInscripciones:
    __inscripciones= None
    __cantidadInscriptos= 0
    __dimension= 0
    __incremento= 5
    
    def __init__(self):
        self.__inscripciones= np.empty(self.__dimension,dtype=Inscripcion)
        
    def addInscripto(self,inscripto):
        if self.__dimension == self.__cantidadInscriptos:
            self.__dimension+= self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidadInscriptos]= inscripto
        self.__cantidadInscriptos+= 1
        
    def consultarInscripcion_y_montoPendiente(self,dni):
        i= 0
        bandera= False
        while not bandera and i < self.__cantidadInscriptos:
            persona_Inscripta= self.__inscripciones[i].getPersona()
            if persona_Inscripta.getDni() == dni:
                bandera= True
                taller= self.__inscripciones[i].getTaller()
                monto= self.__inscripciones[i].getPago()
                if monto:
                    print("El inscripto no tiene pagos pendientes")
                else: 
                    print(f"El sr/a {persona_Inscripta.getNombre()} DNI: {persona_Inscripta.getDni()} inscripto en el {taller.getNombreTaller()} adeuda ${taller.getMonto()}")
            i+= 1
        if not bandera: print("No se encontró el dni ingresado")
        
    def registrarPago(self,dni):
        i= 0
        bandera= False
        while not bandera and i < self.__cantidadInscriptos:
            persona_Inscripta= self.__inscripciones[i].getPersona()
            if persona_Inscripta.getDni() == dni:
                bandera= True
                self.__inscripciones[i].updatePago()
                
    def guardarInscripciones_enArchivo(self):
        iterable= []  
        cabeza= []         
        with open ("Inscripciones Talleres.csv",'w',encoding="utf8") as new_archivo:
            writer= csv.writer(new_archivo,delimiter=';')
            cabeza.append("DNI")
            cabeza.append("idTaller")
            cabeza.append("fechaInscripción")
            cabeza.append("pago")
            writer.writerow(cabeza)
            for i in range(self.__cantidadInscriptos):
                persona= self.__inscripciones[i].getPersona()
                taller= self.__inscripciones[i].getTaller()
                dni= persona.getDni()
                iterable.append(dni)
                id= taller.getIdTaller()
                iterable.append(id)
                fecha= self.__inscripciones[i].getFechaInscripcion()
                iterable.append(fecha)
                pago= self.__inscripciones[i].getPago()
                iterable.append(pago)
                writer.writerow(iterable)
                iterable.clear()
                
                