from coleccion_vehiculos import ColeccionVehiculos
from object_encoder import ObjectEncoder
from clase_menu import Menu
from interfaz_lista import ILista

if __name__ == "__main__":  
    jsonF= ObjectEncoder()
    coleccion= ColeccionVehiculos()
    menu= Menu(ILista(coleccion),jsonF)    
    menu.generarMenu()