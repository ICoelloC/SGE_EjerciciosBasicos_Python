from sistemas.Control import Control
from utilities.Utils import Utils


class Modulo:
    def __init__(self, robot, comunicacion):
        self.id = Utils.generarint(1, 255)
        self.largo = Utils.generarint(1, 200)
        self.ancho = Utils.generarint(1, 200)
        self.alto = Utils.generarint(1, 200)
        self.robot = robot
        self.control = Control(self, comunicacion)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self, value):
        self.__largo = value

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        self.__ancho = value

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        self.__alto = value

    @property
    def robot(self):
        return self.__robot

    @robot.setter
    def robot(self, itemRobot):
        self.__robot = itemRobot

    @property
    def control(self):
        return self.__control

    @control.setter
    def control(self, sistemaControl):
        self.__control = sistemaControl

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => ID: {1}, Largo: {2}cm, Ancho: {3}cm, Alto: {4}cm"
        return msg.format(clase, self.id, self.largo, self.ancho, self.alto)
