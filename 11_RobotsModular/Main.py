from factorias.FactoriaRobot import FactoriaRobot
from sistemas.Comunicacion import Comunicacion
from utilities.Utils import Utils

comunicacion = Comunicacion()
robot = FactoriaRobot.crearrobot(comunicacion)

print(robot)
print()
opcion = 0
while opcion != 5:
    opcion = Utils.menu()
    Utils.realizar_accion(opcion, robot, comunicacion)
