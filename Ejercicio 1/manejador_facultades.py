import csv
from clase_facultad import Facultad
from clase_carrera import Carrera

class ManejaFacultades:
    __lista_facultades= list
    
    def __init__(self):
        self.__lista_facultades= [] 
        
    def agregar_facultad(self,una_facultad):
        self.__lista_facultades.append(una_facultad)        
        
    def lecturaArchivo(self):
        with open ("Facultades.csv",encoding="utf8") as archivo:
            reader= csv.reader(archivo,delimiter=';')
            for fila in reader:
                string= fila[1]
                codigo= int(fila[0])
                if string.find("Facultad") != -1:
                    nombre= fila[1]
                    direc= fila[2]
                    localidad= fila[3]
                    tel= fila[4]
                    una_facultad= Facultad(codigo,nombre,direc,localidad,tel)
                    self.agregar_facultad(una_facultad)
                else: 
                    codC= codigo,int(fila[1])
                    nombreC= fila[2]
                    duracion= fila[3]
                    titulo= fila[4]
                    una_carrera= Carrera(codC,nombreC,duracion,titulo)
                    self.__lista_facultades[len(self.__lista_facultades)-1].agregarCarrera(una_carrera)
    
    def buscarFacultad(self,codigo):
        i= 0
        bandera= False
        k= None
        while not bandera and i < len(self.__lista_facultades):
            if self.__lista_facultades[i].getCodigo() == codigo:
                print(f"{self.__lista_facultades[i].getNombre()}")
                bandera= True
                k= i
            i+= 1
        return bandera, k
        
    def mostrarInfoCarreras(self,i):
        self.__lista_facultades[i].mostrarCarreras()
        
    def buscarCarrera(self,carrera):
        i= 0
        bandera= False
        k= None
        while not bandera and i < len(self.__lista_facultades):
            resultado, cod= self.__lista_facultades[i].buscar(carrera)
            if resultado:
                k= i
                bandera= True
            i+= 1
        return bandera, cod, k
    
    def mostrar(self,i):
        print(f"{self.__lista_facultades[i].getNombre()}")
        print(f"{self.__lista_facultades[i].getLocalidad()}")
                