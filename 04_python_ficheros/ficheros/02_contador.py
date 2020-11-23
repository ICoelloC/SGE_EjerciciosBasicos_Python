#! /usr/bin/env python
from io import open
import sys

if __name__ == '__main__':
    fichero = open("utilidades/monitorContador.txt", "a+")
    fichero.seek(0)
    contenido = fichero.readline()
    if len(contenido) == 0:
        contenido = "0"
        fichero.write(contenido)
    fichero.close()
    try:
        contador = int(contenido)
        if len(sys.argv) == 2:
            if sys.argv[1] == "inc":
                contador += 1
            elif sys.argv[1] == "dec":
                contador -= 1
        print(contador)
        fichero = open("utilidades/monitorContador.txt", "w")
        fichero.write(str(contador))
        fichero.close()
    except:
        print("Error: Fichero corrupto.")
