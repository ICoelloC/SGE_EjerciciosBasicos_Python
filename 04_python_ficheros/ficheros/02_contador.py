#! /usr/bin/env python
from io import open
import sys

if __name__ == '__main__':
    fichero = open("utilidades/monitorContador.txt", "a+")
    contenido = fichero.readline()
    if len(contenido) == 0:
        contenido = "0"
        fichero.write(contenido)
    contador = int(contenido)
    if sys.argv[0] == "inc":
        contador += 1
    elif sys.argv[0] == "dec":
        contador -= 1
    print(contador)
    fichero.write(str(contador))
    fichero.close()
