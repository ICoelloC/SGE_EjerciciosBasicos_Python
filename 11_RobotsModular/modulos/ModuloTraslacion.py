from modulos.Modulo import Modulo
from motores.MotorTraslacion import MotorTraslacion


class ModuloTraslacion(Modulo):

    def __init__(self, robot, comunicacion):
        super().__init__(robot, comunicacion)
        self.motor = MotorTraslacion()

    def mover(self):
        self.motor.funcionar()

    def __str__(self):
        return super().__str__()
