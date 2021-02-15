from motores.Motor import Motor
from utilities.Utils import Utils


class MotorTraslacion(Motor):

    def __init__(self):
        super().__init__()
        self.posx = 0

    @property
    def posx(self):
        return self.__posx

    @posx.setter
    def posx(self, value):
        self.__posx = value

    def funcionar(self):
        self.posx = Utils.generarint(1, 40)

    def __str__(self):
        clase = type(self).__name__
        return super.__str__(self) + f", {clase}, Posx: {self.posx}"
