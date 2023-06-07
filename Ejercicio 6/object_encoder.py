from coleccion_vehiculos import ColeccionVehiculos
from clase_nuevo import Nuevo
from clase_usado import Usado
from clase_nodo import Nodo
from pathlib import Path
import json

class ObjectEncoder:
    
    def decodificarDiccionario(self,d):
        if "__class__" not in d:
            resultado= d
        else:
            class_name= d['__class__']
            class_= eval(class_name)
            if class_name == 'ColeccionVehiculos':
                nodos= d['nodos']
                dNodo= nodos[0]
                coleccion= class_()
                for i in range(len(nodos)):
                    dNodo= nodos[i]
                    class_name= dNodo.pop('__class__')
                    class_= eval(class_name)
                    atributosN= dNodo['__atributos__']
                    v= atributosN['vehiculo']
                    class_name= v.pop('__class__')
                    class_= eval(class_name)
                    atributos= v['__atributos__']
                    if class_name == "Nuevo":
                        vehiculo= Nuevo(**atributos)
                    else:
                        vehiculo= Usado(**atributos)
                    coleccion.agregarElementoalFinal(vehiculo)
            resultado= coleccion
        return resultado
                
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open ('w') as destino:
            json.dump(diccionario,destino,indent=4)
    
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open (encoding="utf8") as fuente:
            diccionario= json.load(fuente)
        return diccionario