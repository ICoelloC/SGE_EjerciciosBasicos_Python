import random

from utilities import Constantes


class Utils:

    @staticmethod
    def generarint(min, max):
        return random.randint(min, max)

    @staticmethod
    def generartipo():
        tipos = [Constantes.TIPO1, Constantes.TIPO2]
        return tipos[Utils.generarint(0, 1)]

    @staticmethod
    def menu():
        global opcion
        print("1. Usar Módulo Estático")
        print("2. Usar Módulo Rotación")
        print("3. Usar Módulo Traslación")
        print("4. Usar Módulo Helicoidal")
        print("5. Mostrar Información")
        valor_correcto = False
        while not valor_correcto:
            try:
                opcion = int(input("Opción: "))
                if opcion < 1 or opcion > 5:
                    print("El valor introducido no es correcto")
                else:
                    valor_correcto = True
            except ValueError:
                print("El valor introducido no es correcto")
        return opcion

    @staticmethod
    def realizar_accion(opcion, robot, comunicacion):
        try:
            if opcion == 1:
                robot.modulos[0].control.captar()
                if len(robot.modulos[0].sensores) < 1:
                    print("El módulo estatico no tiene sensores\r\n")
                else:
                    print("El módulo estatico ha captado información\r\n")
            elif opcion == 2:
                robot.modulos[1].control.mover()
                print("El módulo de rotación ha girado\r\n")
            elif opcion == 3:
                robot.modulos[2].control.mover()
                print("El módulo de traslación se ha movido\r\n")
            elif opcion == 4:
                robot.modulos[3].control.mover()
                print("El módulo helicoidal se ha movido y girado\r\n")
            elif opcion == 5:
                print("Mostrando la información obtenida\r\n")
                print(str(comunicacion))
        except ValueError as e:
            print(e)
