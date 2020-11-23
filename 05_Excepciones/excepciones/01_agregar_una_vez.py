#! /usr/bin/env python

def agregar_una_vez(lista, valor):
    try:
        if valor in lista:
            raise ValueError
        else:
            lista.append(valor)
    except ValueError:
        print("Ya exite un valor igual que '", valor, "' en la lista")


if __name__ == '__main__':
    valores = []
    agregar_una_vez(valores, 'Hola')
    agregar_una_vez(valores, 'mundo')
    agregar_una_vez(valores, 'esto')
    agregar_una_vez(valores, 'es')
    agregar_una_vez(valores, 'un')
    agregar_una_vez(valores, 'ejemplo')
    agregar_una_vez(valores, 'de')
    agregar_una_vez(valores, 'control')
    agregar_una_vez(valores, 'de')
    agregar_una_vez(valores, 'excepciones')
