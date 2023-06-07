from clase_menu import Menu
from manejador_facultades import ManejaFacultades

if __name__ == '__main__':
    manejador_facultades= ManejaFacultades()
    manejador_facultades.lecturaArchivo()
    menu= Menu(manejador_facultades)
    menu.generarMenu()