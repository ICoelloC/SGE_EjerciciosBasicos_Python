from modulos.Modulo import Modulo
from motores.MotorRotacion import MotorRotacion


class ModuloRotacion(Modulo):

    def __init__(self, robot, comunicacion):
        super().__init__(robot, comunicacion)
        self.motor = MotorRotacion()

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, value):
        self.__motor = value

    def mover(self):
        self.motor.funcionar()

    def __str__(self):
        return super().__str__()
