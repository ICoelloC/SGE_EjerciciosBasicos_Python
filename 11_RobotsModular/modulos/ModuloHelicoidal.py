from modulos.Modulo import Modulo


class ModuloHelicoidal(Modulo):

    def __init__(self, robot, comunicacion):
        super().__init__(robot, comunicacion)
        self.motor = []

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, value):
        self.__motor = value

    def mover(self):
        for i in self.motor:
            i.funcionar()

    def __str__(self):
        return super().__str__()
