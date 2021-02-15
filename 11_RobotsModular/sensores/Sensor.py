from utilities import Constantes
from utilities.Utils import Utils


class Sensor:

    def __init__(self):
        self.id = Utils.generarint(1, 200)
        self.tipo = Utils.generartipo()

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def captarinformacion(self):
        if self.tipo == Constantes.TIPO1:
            valor = f"ID: {self.id}, {Constantes.TIPO1}: {Utils.generarint(0, 50)}{Constantes.GRADOS}"
        else:
            valor = f"ID: {self.id}, {Constantes.TIPO2}: {Utils.generarint(0, 100)}{Constantes.PORCENTAJE}"
        return valor
