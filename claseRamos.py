

class ramo:
    __tamaño = ''
    __lista_flores = []
    def __init__(self, t):
        self.__tamaño = t
        self.__lista_flores =[]
    def __str__(self):
        v = ''
        v = self.__tamaño + '\n'
        v += 'flores del ramo:' + '\n'
        for elem in self.__lista_flores:
            v += str(elem)
            v += "\n"
        return v

    def get_tamaño(self):
        return self.__tamaño

    def get_flor(self):
            return self.__lista_flores

    def agregar_flor(self, f):
        self.__lista_flores.append(f)