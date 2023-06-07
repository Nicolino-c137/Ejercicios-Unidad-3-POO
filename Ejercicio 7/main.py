from coleccion import Coleccion
from clase_menu import Menu
from interfaz_lista import ILista
from object_encoder import ObjectEncoder

if __name__ == "__main__":
    coleccion= Coleccion()
    jsonF= ObjectEncoder()
    menu= Menu(ILista(coleccion),jsonF)
    menu.generarMenu()