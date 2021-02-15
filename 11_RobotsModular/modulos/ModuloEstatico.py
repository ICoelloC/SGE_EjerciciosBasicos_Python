from modulos.Modulo import Modulo


class ModuloEstatico(Modulo):

    def __init__(self, robot, comunicacion):
        super().__init__(robot, comunicacion)
        self.sensores = []

    @property
    def sensores(self):
        return self.__sensores

    @sensores.setter
    def sensores(self, value):
        self.__sensores = value

    def addsensor(self, sensor):
        self.sensores.append(sensor)

    def captarinformacion(self):
        mensaje = f""
        for i in self.sensores:
            mensaje += f"\r\nTipo Sensor: {i.tipo}, {i.captarinformacion()}"
        return mensaje

    def __str__(self):
        return super().__str__() + f", Sensores: {len(self.sensores)}"
