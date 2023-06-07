from interfaz_director import IDirector
import sys, os

class Menu:
    __elecciones= {}
    
    def __init__(self,ManejarDirector: IDirector):
        self.__manejarDirector= ManejarDirector
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Modificar Sueldo Basico de Agente
2. Modificar porcentaje por cargo de Docente
3. Modificar porcentaje por categoria a Personal de Apoyo
4. Modificar porcentaje extra a Docente Investigador
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
        dni= input("DNI del agente: ")
        nuevoBasico= int(input("Ingrese el nuevo Sueldo Básico: "))
        self.__manejarDirector.modificarBasico(dni,nuevoBasico)
        os.system("pause")
        
    def opcion2(self):
        dni= input("DNI del agente: ")
        nuevoPorcentaje= float(input("Ingrese el nuevo porcentaje: "))
        self.__manejarDirector.modificarPorcentajeporcargo(dni,nuevoPorcentaje)
        os.system("pause")
        
    def opcion3(self):
        dni= input("DNI del agente: ")
        nuevoPorcentajeCategoria= float(input("Ingrese el nuevo porcentaje por categoria: "))
        self.__manejarDirector.modificarPorcentajeporcategoria(dni,nuevoPorcentajeCategoria)
        os.system("pause")
        
    def opcion4(self):
        dni= input("DNI del agente: ")
        nuevoImporteExtra= int(input("Ingrese el nuevo importe extra: "))
        self.__manejarDirector.modificarImporteExtra(dni,nuevoImporteExtra)
        os.system("pause")
                
    def salir(self):
        sys.exit(0)