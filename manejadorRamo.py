from claseRamos import ramo
import os

class manR:
    __lista = []
    def __init__(self):
        self.__lista = []
    
    def agregar_ramo(self, flores):
        print("listado de flores".center(30,'-'))
        for elem in (flores.listar()):
            print("{}".format(elem))
        print("\n")
        print("ingrese tamaño de ramo('chico','mediano','grande')")
        t = input()
        r = ramo(t)
        print("ingrese codigo de flor a agregar(finalice con -1)")
        n = int(input())
        while n != -1 :
            print("ingrese cantidad a agregar de la flor: {}".format(n))
            cant = int(input())
            flor = flores.buscar_flor(n)
            for i in range(cant):
                r.agregar_flor(flor)
            n = int(input("ingrese codigo de flor a agregar(finalice con -1)"))
        self.__lista.append(r)
    
    def listado(self):
        ant = None
        t = input("ingrese tamaño de ramo a buscar (chico, mediano, grande)")
        print("listado de flores para el ramo de tamaño: {}".format(t))
        for elem in self.__lista:
            if elem.get_tamaño() == t:
                for flor in elem.get_flor():
                    if ant != flor:
                        print("".center(10,'-'))
                        print("{}".format(flor))
                        ant = flor
            
    def imprimir(self):
        for elem in self.__lista:
            print("{}".format(elem))
