from clase_inscripcion import Inscripcion
from datetime import date
import sys, os

class Menu:
    __elecciones= {}
    __mTalleres= object
    __mInscripciones= object
    __mPersonas= object
    
    def __init__(self,m_inscripciones,m_talleres,m_personas):
        self.__mInscripciones= m_inscripciones
        self.__mTalleres= m_talleres
        self.__mPersonas= m_personas
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Inscribir persona en un taller
2. Consultar inscripción
3. Consultar inscriptos
4. Registrar pago
5. Guardar inscripciones
0. Salir
""")
        
    def generarMenu(self):
        while True:
            self.mostrarMenu()
            op= input("Seleccion alguna opción: ")
            os.system("cls")
            ejecutar= self.__elecciones.get(op)
            if ejecutar:
                ejecutar()
            else: 
                print("Opcion no valida, vuelva a intentarlo")
                os.system("pause")
            
    def opcion1(self):
        print("Inscripción de Personas")
        persona= self.__mPersonas.cargarDatosPersona()
        self.__mTalleres.mostrarTalleresDisponibles()
        id= int(input("Elija el taller al que desea inscribirse: "))
        taller= self.__mTalleres.buscar_y_retornarTaller(id)
        if taller != None:
            fecha= date.today()
            inscripto= Inscripcion(fecha,False,persona,taller)
            self.__mTalleres.inscribirPersona(inscripto,taller)
            self.__mInscripciones.addInscripto(inscripto)
        else: print("Opción no válida. Vuelva a intentarlo")
        os.system("pause")
           
    def opcion2(self):
        print("2. Consultar inscripción")
        print()
        dni= input("Ingrese el dni de una persona para mostrar el monto que adeuda y el taller inscripto: ")
        self.__mInscripciones.consultarInscripcion_y_montoPendiente(dni)
        os.system("pause")
    
    def opcion3(self):
        print("3. Consultar inscriptos")
        print()
        id= int(input("Ingrese el id de un taller para listar los alumnos inscriptos en él: "))
        resultado= self.__mTalleres.verificarExistenciaTaller(id)
        if resultado:
            self.__mTalleres.listarAlumnosInscriptos(id)
        else: print("No se encontró la id del taller ingresado")
        os.system("pause")
        
    def opcion4(self):
        print("4. Registrar pago")
        print()
        dni= input("Ingrese el dni de una persona para registrar su pago: ")
        self.__mInscripciones.registrarPago(dni)
        os.system("pause")
        
    def opcion5(self):
        print("5. Guardar inscripciones")
        print()
        self.__mInscripciones.guardarInscripciones_enArchivo()
        print("Operación realizada con éxito!")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)