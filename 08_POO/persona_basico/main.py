#! usr/bin/env python
from persona import Persona

if __name__ == '__main__':
    persona1 = Persona()
    persona1.inicializar("Ivan", 23)

    persona2 = Persona()
    persona2.inicializar("Carlos", 17)

    # imprimimos datos y comprobamos si es mayor de edad
    persona1.imprimir()
    persona1.mayor_edad()

    persona2.imprimir()
    persona2.mayor_edad()
