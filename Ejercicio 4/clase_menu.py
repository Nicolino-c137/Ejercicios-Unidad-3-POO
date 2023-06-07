from datetime import date
import sys, os

class Menu:
    __elecciones= {}
    __coleccionEmpleados= object
    
    def __init__(self,empleados):
        self.__coleccionEmpleados= empleados
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

1. Registrar horas
2. Mostrar monto a pagar de una tarea
3. Dar ayuda económica
4. Calcular sueldo de todos los empleados
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
        print("1. Registrar horas")
        print()
        dni= input("Ingrese el dni del empleado: ")
        resultado, indice= self.__coleccionEmpleados.buscarEmpleado(dni)
        if resultado:
            horas= int(input("Ingrese la cantidad de horas trabajadas en el día de la fecha: "))
            self.__coleccionEmpleados.incrementarHorasTrabajadas(horas,indice)
        else: print("No se econtró el dni ingresado. Vuelva a intentarlo")
        os.system("pause")
           
    def opcion2(self):
        print("2. Mostrar monto a pagar de una tarea")
        print()
        tarea= input("Ingrese una tarea para ver el monto a pagar: ")
        resultado=self.__coleccionEmpleados.verificarExistenciaTarea(tarea)
        if resultado:
            fechaActual= str(date.today())
            self.__coleccionEmpleados.verificarFecha_y_mostrarMonto(fechaActual,tarea)
        else: print("No se encontró la tarea ingresada. Vuelva a intentarlo")
        os.system("pause")
    
    def opcion3(self):
        print("3. Dar ayuda económica")
        print()
        self.__coleccionEmpleados.listarEmpleados_que_necesitanAyudaEconomica()
        os.system("pause")
        
    def opcion4(self):
        print("4. Calcular sueldo de todos los empleados")
        print()
        self.__coleccionEmpleados.mostrarEmpleados_con_sueldo_a_cobrar()
        os.system("pause")
    
    def salir(self):
        sys.exit(0)