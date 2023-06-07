from manejador_sabores import ManejaSabores
from manejador_helados import ManejaHelados
from clase_menu import Menu

if __name__ == '__main__':
    manejadorSabores= ManejaSabores()
    manejadorHelados= ManejaHelados()
    manejadorSabores.lecturaArchivo()
    menu= Menu(manejadorSabores,manejadorHelados)
    menu.generarMenu()