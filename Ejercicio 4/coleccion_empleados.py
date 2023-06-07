from clase_empleado import Empleado
from clase_planta import Planta
from clase_contratado import Contratado
from clase_externo import Externo
import numpy as np
import csv

class ColeccionEmpleados:
    __cantidadEmpleados= 0
    __empleados= None 
    
    def __init__(self,dimension):
        self.__empleados= np.empty(dimension,dtype=Empleado)
        
    def addEmpleado(self,un_empleado):
        self.__empleados[self.__cantidadEmpleados]= un_empleado
        self.__cantidadEmpleados+= 1
        
    def lecturaArchivos(self,x):
        with open (x,encoding="utf8") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                if x == "Planta.csv":
                    un_empleado= Planta(*fila)
                    self.addEmpleado(un_empleado)
                elif x == "Contratados.csv":
                    un_empleado= Contratado(*fila)
                    self.addEmpleado(un_empleado)
                elif x == "Externos.csv":
                    un_empleado= Externo(*fila)
                    self.addEmpleado(un_empleado)
     
    def buscarEmpleado(self,dni):
        i= 0
        k= None
        bandera= False
        while not bandera and i < self.__cantidadEmpleados:
            if self.__empleados[i].getDni() == dni:
                bandera= True
                k= i
            i+= 1
        return bandera, k
    
    def incrementarHorasTrabajadas(self,horas,i):
        self.__empleados[i].updateHorasTrabajadas(horas)
        
    def verificarExistenciaTarea(self,tarea):
        i= 0
        bandera= False
        while not bandera and i < self.__cantidadEmpleados:
            if isinstance(self.__empleados[i],Externo):
                if self.__empleados[i].getTarea() == tarea:
                    bandera= True
            i+= 1
        return bandera
    
    def verificarFecha_y_mostrarMonto(self,fechaActual,tarea):
        for i in range(self.__cantidadEmpleados):
            if isinstance(self.__empleados[i],Externo):
                if self.__empleados[i].getTarea() == tarea:
                    if fechaActual < self.__empleados[i].getFechaFinalizacion():
                        print(f"${self.__empleados[i].getCostoObra()} es el monto a pagar por la tarea")
                    else: print("Tarea finalizada")
                    
    def listarEmpleados_que_necesitanAyudaEconomica(self):
        print("Los siguientes empleados necesitan una ayuda económica:")
        print("{:^20} {:^20} {:^15}".format("Nombre","Dirección","DNI"))
        print("-------------------------------------------------------")
        for i in range(self.__cantidadEmpleados):
            if self.__empleados[i].calcularSueldo() < 150000:
                print("{:^20} {:^20} {:^15}".format(self.__empleados[i].getNombre(),self.__empleados[i].getDireccion(),self.__empleados[i].getDni()))
                
    def mostrarEmpleados_con_sueldo_a_cobrar(self):
        print("{:^20} {:^15} {:<15}".format("Nombre","Telefono","Sueldo"))
        print("------------------------------------------------------")
        for i in range(self.__cantidadEmpleados):
            print("{:^20} {:^15} ${:<15}".format(self.__empleados[i].getNombre(),self.__empleados[i].getTelefono(),self.__empleados[i].calcularSueldo()))