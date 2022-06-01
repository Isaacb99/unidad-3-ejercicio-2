from tkinter import N

class  flores:
    __numero = 0
    __nombre = ''
    __color = ''
    __descripcion = ''
    def __init__(self, n, nom, c ,d):
        self.__numero = n
        self.__nombre = nom
        self.__color = c
        self.__descripcion = d
    def __str__(self):
        return "numero: {}, nombre: {}, color: {}, descricion: {}".format(self.__numero, self.__nombre, self.__color, self.__descripcion)
    
    def get_num(self):
        return self.__numero