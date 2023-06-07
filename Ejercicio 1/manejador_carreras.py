class Manejador_Carreras:
    __lista_carreras= list
    
    def __init__(self):
        self.__lista_carreras= []
        
    def agregarCarrera(self,una_carrera):
        self.__lista_carreras.append(una_carrera)
        
    def mostrarNombreyDuracion(self):
        for i in range(len(self.__lista_carreras)):
            nombre= self.__lista_carreras[i].getNombre()
            duracion= self.__lista_carreras[i].getDuracion()
            print(f"Carrera: {nombre} | Duración: {duracion}")
            
    def buscarCarrera(self,carrera):
        i= 0
        bandera= False
        codigo= None
        while not bandera and i < len(self.__lista_carreras):
            if self.__lista_carreras[i].getNombre() == carrera:
                codigo= self.__lista_carreras[i].getCodigo()
                bandera= True
            i+= 1
        return bandera, codigo