from manejadorFlores import manF
import os

from manejadorRamo import manR

class menu:
    __op = 0
    __lista_flores = None
    __lista_ramos = None
    def __init__(self, p=0):
        self.__op =p
        self.__lista_flores = manF()
        self.__lista_ramos = manR()
    def opciones(self):
        self.__lista_flores.carga()
        salir = True
        while salir:
            print("MENU".center(14,'-'))
            print("opcion 1: agregar ramo vendido")
            print("opcion 2: mostrar las 5 flores mas vendidas de cada ramo vendido")
            print("opcion 3: mostrar las flores vendidas para los ramos vendidos")
            print("opcion 4: SALIR DEL PROGRAMA")
            self.__op = int(input("ingrese opcion a ejecutar"))
            os.system('cls')
            if self.__op == 1:
                self.__lista_ramos.agregar_ramo(self.__lista_flores)
            elif self.__op == 2:
                print("////")
            elif self.__op == 3:
                self.__lista_ramos.listado()
            elif self.__op == 4:
                salir = not salir
                print("terminando ejecucion de programa")
            else: print("///opcion incorrecta///")