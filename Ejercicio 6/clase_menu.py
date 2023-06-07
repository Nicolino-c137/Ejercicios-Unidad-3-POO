from clase_usado import Usado
from clase_nuevo import Nuevo

import sys, os

class Menu:
    __elecciones= {}
    
    def __init__(self,coleccion,jsonF):
        self.__coleccion_v= coleccion
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
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Leer archivo JSON
2. Insertar vehículo en la colección en una posicion determinada
3. Agregar vehículo a la colección
4. Mostrar tipo de objeto que se encuentra almacenado en una posicion ingresada
5. Modificar precio base y mostrar precio de venta de un vehículo usado según la patente ingresada
6. Mostrar todos los datos del vehículo más económico
7. Mostrar modelo, cantidad de puertas e importe de venta de todos los vehículos que la concesionaria tiene a la venta
8. Almacenar objetos de la colección en el archivo "vehiculos.json"
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
        diccionario = self.__jsonF.leerJSONArchivo("vehiculos.json")
        self.__coleccion_v= self.__jsonF.decodificarDiccionario(diccionario)
        print("Lectura exitosa!")
        os.system("pause")
           
    def opcion2(self):
        print("2. Insertar vehículo en la colección en una posicion determinada")
        print()
        tipo= input("Elija el tipo de vehículo a cargar: ")
        if tipo == "Nuevo":
            posicion= int(input("Ingrese la posición donde desea insertar el vehículo: "))
            print("Ingrese los datos del vehículo")
            marca= input("Marca: ")
            modelo= input("Modelo: ")
            version= input("Versión: ")
            cantPuertas= int(input("Cantidad de puertas: "))
            color= input("Color: ")
            precioBase= int(input("Precio base: "))
            vehiculo= Nuevo(marca,modelo,cantPuertas,color,precioBase,version)
            self.__coleccion_v.insertarElementoPosicionDeseada(vehiculo,posicion)
        elif tipo == "Usado":
            posicion= int(input("Ingrese la posición donde desea insertar el vehículo: "))
            print("Ingrese los datos del vehículo")
            marca= input("Marca: ")
            modelo= input("Modelo: ")
            cantPuertas= int(input("Cantidad de puertas: "))
            color= input("Color: ")
            precioBase= int(input("Precio base: "))    
            patente= input("Patente: ") 
            año= int(input("Año: "))
            km= int(input("Kilometraje: "))   
            vehiculo= Usado(marca,modelo,cantPuertas,color,precioBase,patente,año,km)
            self.__coleccion_v.insertarElementoPosicionDeseada(vehiculo,posicion)
        os.system("pause")
    
    def opcion3(self):
        print("3. Agregar vehículo a la colección")
        print()
        tipo= input("Elija el tipo de vehículo a cargar: ")
        if tipo== "Nuevo":
            print("Ingrese los datos del vehículo")
            marca= input("Marca: ")
            modelo= input("Modelo: ")
            version= input("Versión: ")
            cantPuertas= int(input("Cantidad de puertas: "))
            color= input("Color: ")
            precioBase= int(input("Precio base: "))
            vehiculo= Nuevo(marca,modelo,cantPuertas,color,precioBase,version)
            self.__coleccion_v.agregarElementoalFinal(vehiculo)
        elif tipo == "Usado":
            print("Ingrese los datos del vehículo")
            marca= input("Marca: ")
            modelo= input("Modelo: ")
            cantPuertas= int(input("Cantidad de puertas: "))
            color= input("Color: ")
            precioBase= int(input("Precio base: "))    
            patente= input("Patente: ") 
            año= int(input("Año: "))
            km= int(input("Kilometraje: "))   
            vehiculo= Usado(marca,modelo,cantPuertas,color,precioBase,patente,año,km)
            self.__coleccion_v.agregarElementoalFinal(vehiculo)
        os.system("pause")
        
    def opcion4(self):
        print("4. Mostrar tipo de objeto que se encuentra almacenado en una posicion ingresada")
        print()
        posicion= int(input("Ingrese la posicion: "))
        self.__coleccion_v.mostrarElemento(posicion)
        os.system("pause")
    
    def opcion5(self):
        print("5. Modificar precio base y mostrar precio de venta de un vehículo usado según la patente ingresada")
        print()
        patente= input("Ingrese la patente del vehículo: ")
        resultado= self.__coleccion_v.verificarExistenciaPatente(patente)
        if resultado: 
            nuevo_precio= int(input("Ingrese el nuevo precio: "))
            self.__coleccion_v.modificarPrecioBase_segunPatenteIngresada(patente,nuevo_precio)
            self.__coleccion_v.mostrarPrecioVenta_segunPatenteIngresada(patente)
        else: print("No se encontró la patente ingresada")
        os.system("pause")
        
    def opcion6(self):
        print("6. Mostrar todos los datos del vehículo más económico")
        print()
        importe= self.__coleccion_v.buscarVehiculoEconomico()
        self.__coleccion_v.mostrarDatosVehiculo_segunImporte(importe)
        os.system("pause")
        
    def opcion7(self):
        print("7. Mostrar modelo, cantidad de puertas e importe de venta de todos los vehículos que la concesionaria tiene a la venta")
        print()
        self.__coleccion_v.mostrarTodoslosVehiculosDisponibles()
        os.system("pause")
        
    def opcion8(self):
        print("8. Almacenar objetos de la colección en el archivo 'vehiculos.json'")
        print()  
        d= self.__coleccion_v.toJSON()
        self.__jsonF.guardarJSONArchivo(d,"vehiculos.json")
        print("Archivo creado con éxito!")
        os.system("pause")      
    
    def salir(self):
        sys.exit(0)