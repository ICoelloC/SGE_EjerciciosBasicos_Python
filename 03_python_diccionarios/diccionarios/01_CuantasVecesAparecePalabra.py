#!/usr/bin/env python
if __name__ == '__main__':
    cadena = input("Introduce la cadena: ")

    palabras = cadena.split(" ")

    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    for palabra, apariciones in diccionario.items():
        print(palabra, ":", apariciones)
