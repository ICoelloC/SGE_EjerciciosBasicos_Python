#! usr/bin/env python
from alumno import Alumno

if __name__ == '__main__':

    #bloque principal
    # creamos los nuevos objetos
    alumno1 = Alumno("ivan", 8)
    alumno2 = Alumno("maria", 9)
    alumno3 = Alumno("marcos", 4)

    # imprimimos los datos y resultados de cada alumno
    alumno1.imprimir()
    alumno1.resultado()
    alumno2.imprimir()
    alumno2.resultado()
    alumno3.imprimir()
    alumno3.resultado()
