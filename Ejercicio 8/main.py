from coleccion import Coleccion
from clase_menu import Menu
from interfaz_lista import ILista
from interfaz_director import IDirector
from interfaz_tesorero import ITesorero
from object_encoder import ObjectEncoder

def tesorero(ManejarTesorero: ITesorero):
    DNI= input("Ingrese el dni de un agente: ")
    ManejarTesorero.gastosSueldoPorEmpleado(DNI)

if __name__ == "__main__":
    coleccion= Coleccion()
    jsonF= ObjectEncoder()
    menu= Menu(ILista(coleccion),jsonF)
    menu.generarMenu()
    print("Ingrese el nombre de usuario y contraseña para acceder a su interfaz")
    usuario= input("Usuario: ")
    clave= input("Contraseña: ")
    if usuario.lower() == "uTesoreso".lower() and clave == "ag@74ck":
        tesorero(ITesorero(coleccion))
    elif usuario.lower() == "uDirector".lower() and clave == "ufC77#!1":    
        menuDir= Menu(IDirector(coleccion))
        menuDir.generarMenu()
    else: print("Usuario o contraseña ingresado incorrecto")