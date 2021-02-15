from utilities import Constantes


class Control:

    def __init__(self, modulo, comunicacion):
        self.comunicacion = comunicacion
        self.modulo = modulo

    def mover(self):
        self.modulo.mover()
        if type(self.modulo).__name__ == "ModuloTraslacion":
            msg = f"\tMovimiento realizado: {Constantes.MOVIMIENTOTRAS}, avanzado: {self.modulo.motor.posx}{Constantes.MEDIDA}"
            self.comunicacion.recibir(self.modulo, msg)
        elif type(self.modulo).__name__ == "ModuloRotacion":
            msg = f"\tMovimiento realizado: {Constantes.MOVIMIENTOROT}, giro: {self.modulo.motor.angulo}{Constantes.GRADOS}"
            self.comunicacion.recibir(self.modulo, msg)
        else:
            posx = ""
            angulo = ""
            for i in self.modulo.motor:
                if type(i).__name__ == "MotorTraslacion":
                    posx = i.posx
                else:
                    angulo = i.angulo
            msg = f"\tMovimiento realizado: {Constantes.MOVIMIENTOHELI}, avanzado: {posx}{Constantes.MEDIDA}, " \
                  f"giro: {angulo}{Constantes.GRADOS}"
            self.comunicacion.recibir(self.modulo, msg)

    def captar(self):
        self.comunicacion.recibir(self.modulo, self.modulo.captarinformacion())


