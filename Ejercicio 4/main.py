from clase_menu import Menu
from coleccion_empleados import ColeccionEmpleados

if __name__ == "__main__":
    cant= int(input("Ingrese la cantidad de empleados de su empresa: "))
    coleccionEmpleados= ColeccionEmpleados(cant)
    archi= "Planta.csv"
    coleccionEmpleados.lecturaArchivos(archi)
    archi= "Contratados.csv"
    coleccionEmpleados.lecturaArchivos(archi)
    archi= "Externos.csv"
    coleccionEmpleados.lecturaArchivos(archi)
    menu= Menu(coleccionEmpleados)
    menu.generarMenu()