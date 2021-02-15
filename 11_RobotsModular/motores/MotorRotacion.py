from motores.Motor import Motor
from utilities.Utils import Utils


class MotorRotacion(Motor):

    def __init__(self):
        super().__init__()
        self.angulo = 0

    @property
    def angulo(self):
        return self.__angulo

    @angulo.setter
    def angulo(self, value):
        self.__angulo = value

    def funcionar(self):
        self.angulo = Utils.generarint(1, 360)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Movido con un angulo de: {1}"
        return msg.format(clase, self.angulo)
