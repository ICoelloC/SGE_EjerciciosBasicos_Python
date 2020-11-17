#! /usr/bin/env python
import json

if __name__ == '__main__':
    fichero = open("utilidades/personas.json", 'r', encoding="utf8")
    contenido = json.load(fichero)
    print(contenido)
