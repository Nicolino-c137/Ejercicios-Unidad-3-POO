import sys, os

class Menu:
    __elecciones= {}
    
    def __init__(self,manejadorSabores,manejadorHelados):
        self.__manejaSabores= manejadorSabores
        self.__manejaHelados= manejadorHelados
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

1. Registrar venta
2. Mostrar los 5 sabores de helados más pedidos
3. Calcular el total de gramos vendidos de un sabor
4. Mostrar los sabores vendidos según el tipo de helado ingresado
5. Calcular importe total recaudado por cada tipo de helado
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
        print("1. Registrar venta")
        print()
        print("""Seleccione el tipo de helado que desea comprar
100gr       150gr       1000gr
250gr       500gr""")
        gramos= float(input())
        cantSabores= int(input("Elija la cantidad de sabores (Hasta 4 sabores): "))
        self.__manejaSabores.mostrarSaboresDisponibles()
        idSabor= int(input("Elija el sabor que desea: "))
        self.__manejaSabores.incrementarContador(idSabor-1)
        sabor= self.__manejaSabores.getSabor(idSabor)
        self.__manejaHelados.registrarVenta(gramos,sabor,cantSabores,self.__manejaSabores)
        #self.__manejaHelados.mostrarVenta()
        os.system("pause")
           
    def opcion2(self):
        print("2. Mostrar los 5 sabores de helados más pedidos")
        print()
        print("Los 5 sabores mas pedidos son:")
        top5= self.__manejaSabores.calcularTop5Sabores()
        self.__manejaSabores.mostrarSabores(top5)
        os.system("pause")
    
    def opcion3(self):
        print("3. Calcular el total de gramos vendidos de un sabor")
        print()
        id= int(input("Ingrese la id de un sabor para ver cuantos gramos se vendió del mismo: "))
        gramos= self.__manejaHelados.calcularGramos(id)
        if gramos != 0:
            nombre= self.__manejaSabores.getNombreSaborsegunId(id)
            print(f"Se vendió {gramos}gr del sabor {nombre}")
        else: print("No se registraron ventas sobre el sabor ingresado")
        os.system("pause")
        
    def opcion4(self):
        print("4. Mostrar los sabores vendidos según el tipo de helado ingresado")
        print()
        peso= float(input("Ingrese el tipo de helado: "))
        print("Los sabores que se vendieron son:")
        self.__manejaHelados.getSabores_segunTipo(peso,self.__manejaSabores)
        self.__manejaSabores.mostrarCont()
        os.system("pause")
        
    def opcion5(self):
        print("5. Calcular importe total recaudado por cada tipo de helado")
        print()
        t100, t150, t250, t500, t1000= self.__manejaHelados.calcularImporteTotal()
        print(f"""
Para el tipo de helado de 100gr se recaudó ${t100}
Para el tipo de helado de 150gr se recaudó ${t150}
Para el tipo de helado de 250gr se recaudó ${t250}
Para el tipo de helado de 500gr se recaudó ${t500}
Para el tipo de helado de 1000gr se recaudó ${t1000}
En total se recaudó ${t100+t150+t250+t500+t1000}""")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)