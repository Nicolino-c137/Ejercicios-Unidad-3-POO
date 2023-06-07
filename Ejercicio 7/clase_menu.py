import sys, os
from clase_docente import Docente
from clase_docente_investigador import DocenteInvestigador
from clase_investigador import Investigador
from clase_personalApoyo import PersonalApoyo

class Menu:
    __elecciones= {}
    
    def __init__(self,coleccion,jsonF):
        self.__coleccionAgentes= coleccion
        self.__jsonF= jsonF
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '6': self.opcion6,
            '7': self.opcion7,
            '8': self.opcion8,
            '9': self.opcion9,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Leer archivo JSON
2. Insertar agente a la colección
3. Agregar agente a la colección
4. Mostrar el tipo de agente que se encuentra almacenado en la posición ingresada
5. Generar listado con los datos de los docentes investigadores según el nombre de la carrera ingresado por teclado
6. Mostrar cantidad de Docentes Investigadores y cantidad de Investigadores que trabajen en un área de investigación ingresada por teclado
7. Generar listado del personal ordenado por apellido
8. Listar datos de Docentes Investigadores segun la categoría de investigación ingresada por teclado, además mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio
9. Almacenar datos en archivo JSON
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
        print("1. Leer archivo JSON")
        print()
        diccionario= self.__jsonF.leerJSON("personal.json")
        self.__jsonF.decodificarDiccionario(diccionario,self.__coleccionAgentes)
        print("Lectura exitosa!")
        os.system("pause")
           
    def opcion2(self):
        print("2. Insertar agente a la colección")
        print()
        posicion= int(input("Ingrese la posición en la que quiere ingresar el personal: "))
        print("Ingrese los siguientes datos del personal")
        cuil= input("Cuil: ")
        apellido= input("Apellido: ")
        nombre= input("Nombre: ")
        sueldoBasico= int(input("Sueldo Básico: "))
        antiguedad= int(input("Antiguedad: "))
        tipoPersonal= input("Tipo de personal: ")
        if tipoPersonal == "Docente":
            carreraDicta= input("Carrera en la que dicta clases: ")
            cargo= input("Cargo: ")
            catedra= input("Cátedra: ")
            personal= Docente(cuil,apellido,nombre,sueldoBasico,antiguedad,carreraDicta,cargo,catedra)
        elif tipoPersonal == "DocenteInvestigador":
            pass
        elif tipoPersonal == "Investigador":
            areaInvestigacion= input("Área de investigación: ")
            tipoDeInvestigacion= input("Tipo de investigación: ")
            personal= Investigador(cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoDeInvestigacion)
        elif tipoPersonal == "PersonalApoyo":
            categoria= input("Categoría: ")
            personal= PersonalApoyo(cuil,apellido,nombre,sueldoBasico,antiguedad,categoria)
        self.__coleccionAgentes.insertarElementoPosicionDeseada(personal,posicion)
        os.system("pause")
    
    def opcion3(self):
        print("3. Agregar agente a la colección")
        print()
        print("Ingrese los siguientes datos del personal")
        cuil= input("Cuil: ")
        apellido= input("Apellido: ")
        nombre= input("Nombre: ")
        sueldoBasico= int(input("Sueldo Básico: "))
        antiguedad= int(input("Antiguedad: "))
        tipoPersonal= input("Tipo de personal: ")
        if tipoPersonal == "Docente":
            carreraDicta= input("Carrera en la que dicta clases: ")
            cargo= input("Cargo: ")
            catedra= input("Cátedra: ")
            personal= Docente(cuil,apellido,nombre,sueldoBasico,antiguedad,carreraDicta,cargo,catedra)
        elif tipoPersonal == "DocenteInvestigador":
            pass
        elif tipoPersonal == "Investigador":
            areaInvestigacion= input("Área de investigación: ")
            tipoDeInvestigacion= input("Tipo de investigación: ")
            personal= Investigador(cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoDeInvestigacion)
        elif tipoPersonal == "PersonalApoyo":
            categoria= input("Categoría: ")
            personal= PersonalApoyo(cuil,apellido,nombre,sueldoBasico,antiguedad,categoria)
        self.__coleccionAgentes.agregarElementoAlFinal(personal)
        os.system("pause")
        
    def opcion4(self):
        print("4. Mostrar el tipo de agente que se encuentra almacenado en la posición ingresada")
        print()
        posicion= int(input("Ingrese una posición: "))
        self.__coleccionAgentes.mostrarElemento(posicion)
        os.system("pause")
        
    def opcion5(self):
        print("5. Generar listado con los datos de los docentes investigadores según el nombre de la carrera ingresado")
        print()
        carrera= input("Ingrese el nombre de la carrera: ")
        resultado= self.__coleccionAgentes.verificarExistenciaCarrera(carrera)
        if resultado:
            self.__coleccionAgentes.ordenarPorNombre(carrera)
        else: print("No se encontró la carrera ingresada")
        os.system("pause")
        
    def opcion6(self):
        print("6. Mostrar cantidad de Docentes Investigadores, y cantidad de Investigadores que trabajen en un área de investigación ingresada por teclado")
        print()
        area= input("Área de investigación: ")
        resultado= self.__coleccionAgentes.verificarExistenciaArea(area)
        if resultado: 
            self.__coleccionAgentes.mostrarCantidadPersonalSegunAreaInvestigacion(area)
        else: print("No se encontró el área de investigación ingresada")
        os.system("pause")
    
    def opcion7(self):
        print("7. Generar listado del personal ordenado por apellido")
        print()
        self.__coleccionAgentes.ordenarPorApellido()
        os.system("pause")
        
    def opcion8(self):
        print("8. Listar datos de Docentes Investigadores segun la categoría de investigación ingresada por teclado, además mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio")
        print()
        categoria= input("Ingrese la categoría de investigación: ")
        resultado= self.__coleccionAgentes.verificarExistenciaCategoria(categoria)
        if resultado:
            self.__coleccionAgentes.listarDocentesInvestigadoresSegunCategoria(categoria)
        else: print("No se encontró la categoría ingresada")
        os.system("pause")
        
    def opcion9(self):
        print("9. Almacenar datos en archivo JSON")
        print()
        d= self.__coleccionAgentes.toJSON()
        self.__jsonF.guardarJSON(d,"personal.json")
        print("Operación exitosa!")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)