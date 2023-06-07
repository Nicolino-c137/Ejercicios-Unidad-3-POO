class Carrera:
    __codigo= int
    __nombre= str
    __fecha_inicio= 13/3
    __duracion= str
    __titulo= str
    
    def __init__(self,cod,nombre,duracion,titulo):
        self.__codigo= cod
        self.__nombre= nombre
        self.__duracion= duracion
        self.__titulo= titulo
        
    def __str__(self):
        return f"{self.__codigo}, {self.__nombre}, {self.__duracion}, {self.__titulo}"   
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    @classmethod
    def getFechaInicio(cls):
        return cls.__fecha_inicio
    
    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo