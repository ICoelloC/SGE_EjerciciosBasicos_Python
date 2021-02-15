from factorias.FactoriaModulo import FactoriaModulo
from robot.Robot import Robot


class FactoriaRobot:

    @staticmethod
    def crearrobot(comunicacion):
        robot = Robot()
        moduloestatico = FactoriaModulo.crearmoduloestatico(robot, comunicacion)
        modulorotacion = FactoriaModulo.crearmodulorotacion(robot, comunicacion)
        modulotraslacion = FactoriaModulo.crearmodulotraslacion(robot, comunicacion)
        modulohelicoidal = FactoriaModulo.crearmodulohelicoidal(robot, comunicacion)

        robot.modulos.append(moduloestatico)
        robot.modulos.append(modulorotacion)
        robot.modulos.append(modulotraslacion)
        robot.modulos.append(modulohelicoidal)
        return robot
