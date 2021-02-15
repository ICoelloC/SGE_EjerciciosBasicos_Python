class Robot:

    def __init__(self):
        self.modulos = []

    @property
    def modulos(self):
        return self.__modulos

    @modulos.setter
    def modulos(self, listaModulos):
        self.__modulos = listaModulos

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Modulos: {1}"
        modulo = ""
        for i in self.modulos:
            modulo += f"\n {str(i)}"
        return msg.format(clase, modulo)
