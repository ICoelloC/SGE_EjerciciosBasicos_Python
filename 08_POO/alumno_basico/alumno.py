#! usr/bin/env python

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nota(self):
        return self.__nota

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")
