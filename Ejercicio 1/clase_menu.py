import sys, os

class Menu:

    def __init__(self,manejador):
        self.__manejador_facultades= manejador
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Mostrar carreras de una facultad ingresada
2. Mostrar codigo de carrera y facultad donde se dicta
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
        print("1. Mostrar carreras de una facultad ingresada")
        print()
        codigo= int(input("Ingrese el código de una facultad: "))
        resultado, indice= self.__manejador_facultades.buscarFacultad(codigo)
        if resultado:
            self.__manejador_facultades.mostrarInfoCarreras(indice)
        else: print("No se encontró el código ingresado")
        os.system("pause")
           
    def opcion2(self):
        print("2. Mostrar codigo de carrera y facultad donde se dicta")
        print()
        carrera= input("Ingrese el nombre de una carrera: ")
        resultado, codigo, indice= self.__manejador_facultades.buscarCarrera(carrera)
        if resultado:
            print(f"{codigo}")
            self.__manejador_facultades.mostrar(indice)
        else: print("No se encontró la carrera ingresada")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)