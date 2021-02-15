from modulos.ModuloEstatico import ModuloEstatico
from modulos.ModuloTraslacion import ModuloTraslacion
from modulos.ModuloRotacion import ModuloRotacion
from modulos.ModuloHelicoidal import ModuloHelicoidal
from motores.MotorRotacion import MotorRotacion
from motores.MotorTraslacion import MotorTraslacion
from sensores.Sensor import Sensor
from utilities.Utils import Utils


class FactoriaModulo:

    @staticmethod
    def crearmoduloestatico(robot, comunicacion):
        modulo = ModuloEstatico(robot, comunicacion)
        sensores = Utils.generarint(0, 5)
        for i in range(sensores):
            sensor = Sensor()
            modulo.sensores.append(sensor)
        return modulo

    @staticmethod
    def crearmodulotraslacion(robot, comunicacion):
        return ModuloTraslacion(robot, comunicacion)

    @staticmethod
    def crearmodulorotacion(robot, comunicacion):
        return ModuloRotacion(robot, comunicacion)

    @staticmethod
    def crearmodulohelicoidal(robot, comunicacion):
        modulo = ModuloHelicoidal(robot, comunicacion)
        modulo.motor.append(MotorRotacion())
        modulo.motor.append(MotorTraslacion())
        return modulo
