import numpy as np
from claseFlores import flores
import csv

class manF:
    __cantidad = 0
    __dimension = 5
    __incremento = 2
    __flores = None
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 4
        self.__incremento = 2
        self.__flores = np.empty(5, dtype=flores)
    
    def agregar_flores(self, f):
        if isinstance(f, flores):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__flores.resize(self.__dimension)
            self.__flores[self.__cantidad] = f
            self.__cantidad += 1
    
    def carga(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter=';')
        for elem in reader:
            f = flores(int(elem[0]), elem[1], elem[2], elem[3])
            self.agregar_flores(f)
    
    def buscar_flor(self, n):
        i=0
        while i < len(self.__flores) and self.__flores[i].get_num() != n:
            i += 1
        return self.__flores[i]
    
    def listar(self):
        return self.__flores