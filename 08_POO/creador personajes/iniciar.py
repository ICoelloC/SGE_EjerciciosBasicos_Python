from personaje import Personaje

class Iniciar(Personaje):
    def __init__(self):
        self.cargarPersonajes()
        self.interfaz()


Iniciar()