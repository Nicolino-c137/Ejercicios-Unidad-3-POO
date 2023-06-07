from manejador_inscripciones import ManejadorInscripciones
from manejador_personas import ManejadorPersonas
from manejador_talleres import ManejadorTalleres
from clase_taller_capacitacion import TallerCapacitacion
from clase_menu import Menu
import csv

def lecturaNroTalleres():
    archivo= open("Talleres.csv",encoding="utf8")
    talleres= int(archivo.readline())
    archivo.close()
    return talleres

def lecturaDatosTalleres():
    with open ("Talleres.csv",encoding="utf8") as archivo:
        reader= csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            id= int(fila[0])
            nombre= fila[1]
            vacantes= int(fila[2])
            monto= int(fila[3])
            un_Taller= TallerCapacitacion(id,nombre,vacantes,monto)
            manejador_Talleres.agregarTaller(un_Taller)

if __name__ == "__main__":
    dimension_Array_T= lecturaNroTalleres()
    manejador_Talleres= ManejadorTalleres(dimension_Array_T)
    manejador_Personas= ManejadorPersonas()
    manejador_Inscripciones= ManejadorInscripciones()
    lecturaDatosTalleres()
    menu= Menu(manejador_Inscripciones,manejador_Talleres,manejador_Personas)
    menu.generarMenu()