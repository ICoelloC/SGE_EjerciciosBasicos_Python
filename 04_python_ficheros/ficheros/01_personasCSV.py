#! /usr/bin/env python
import csv

if __name__ == '__main__':
    fichero = open("utilidades/personas.csv", 'r', encoding="utf8")
    contenido = csv.reader(fichero)
    for row in contenido:
        print("Registro "+str(contenido.line_num)+" "+str(row))
    fichero.close()
