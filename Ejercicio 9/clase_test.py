from coleccion_vehiculos import ColeccionVehiculos
from interfaz_lista import ILista
from clase_nuevo import Nuevo
from clase_usado import Usado
import unittest

class TestLista(unittest.TestCase):
    __lista= object 
    
    def setUp(self):
        self.__lista= ILista(ColeccionVehiculos())
        v= Usado("Toyota","Supra",2,"Rojo",32500,"AR 420 BR",1998,55631)
        self.__lista.agregarVehiculo(v)
        v1= Usado("Porsche","911 gt3",2,"Amarillo",11500,"AC 123 DE",2020,35000)
        self.__lista.agregarVehiculo(v1)
        v2= Nuevo("BMW","M3 E30",3,"Negro",115000,"Full")
        self.__lista.agregarVehiculo(v2)
        
    def test_insertarVehiculoPosicion0(self):
        v3= Nuevo("BMW","M4",4,"Blanco",119000,"Full")
        self.__lista.insertarElementoPosicionDeseada(v3,1)
        self.assertListEqual(self.__lista.getModelos(),["M4","M3 E30","911 gt3","Supra"])    
        
    def test_insertarVehiculoPosicionIntermedia(self):
        v4= Usado("Subaru","WRX STI",2,"Azul plateado",120299,"DJ 120 MO",2000,135678)
        self.__lista.insertarElementoPosicionDeseada(v4,2)
        self.assertListEqual(self.__lista.getModelos(),["M3 E30","WRX STI","911 gt3","Supra"])
    
    def test_insertarVehiculoPosicionFinal(self):
        v5= Usado("Audi","TT",2,"Blanco",130000,"AM 107 EF",2018,99800)
        self.__lista.agregarElementoalFinal(v5)
        self.assertListEqual(self.__lista.getModelos(),["M3 E30","911 gt3","Supra","TT"])
    
    def test_agregarVehiculoColeccion(self):
        v6= Nuevo("BMW","M3 E36",3,"Gris",118999,"Full")
        self.__lista.agregarVehiculo(v6)
        self.assertListEqual(self.__lista.getModelos(),["M3 E36","M3 E30","911 gt3","Supra"])
    
    def test_obtenerObjetoSegunPosicion(self):
        self.assertTrue(self.__lista.getModeloSegunPosicion(2),"911 gt3")
    
    def test_modificarPrecioBaseYMostrarPrecioVentaSegunPatente(self):
        self.__lista.modificarPrecioBase_segunPatenteIngresada("AR 420 BR",40000)
        self.__lista.mostrarPrecioVenta_segunPatenteIngresada("AR 420 BR")
        self.assertEqual(self.__lista.getImporteVentaSegunPatente("AR 420 BR"),22800)
    
