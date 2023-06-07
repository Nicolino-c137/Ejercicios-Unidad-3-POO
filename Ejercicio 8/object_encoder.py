from coleccion import Coleccion
from clase_nodo import Nodo
from clase_docente import Docente
from clase_docente_investigador import DocenteInvestigador
from clase_investigador import Investigador
from clase_personalApoyo import PersonalApoyo
from pathlib import Path
import json

class ObjectEncoder(object):
    
    def decodificarDiccionario(self,d,coleccion):
        class_name= d["__class__"]
        class_= eval(class_name)
        if class_name == "Coleccion":
            nodos= d["nodos"]
            dnodo= nodos[0]
            for i in range(len(nodos)):
                dnodo= nodos[i]
                class_name= dnodo.pop("__class__")
                class_= eval(class_name)
                atributosN= dnodo["__atributos"]
                a= atributosN["agente"]
                class_name= a.pop("__class__")
                class_= eval(class_name)
                atributos= a["atributos"]
                if class_name == "Docente":
                    agente= Docente(**atributos)
                elif class_name == "DocenteInvestigador":
                    agente= DocenteInvestigador(**atributos)
                elif class_name == "Investigador":
                    agente= Investigador(**atributos)
                elif class_name == "PersonalApoyo":
                    agente= PersonalApoyo(**atributos)
                coleccion.agregarAgente(agente)
    
    def leerJSON(self,archivo):
        with Path(archivo).open(encoding="utf8") as fuente:
            diccionario= json.load(fuente)
        return diccionario
    
    def guardarJSON(self,diccionario,archivo):
        with Path(archivo).open('w',encoding="utf8") as destino:
            json.dump(diccionario,destino,indent=4)