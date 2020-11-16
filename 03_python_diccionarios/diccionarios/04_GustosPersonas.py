#!/usr/bin/env python
if __name__ == '__main__':
    gustosPersonas = {}
    nombre = input("Nombre de la persona: ")
    while nombre != "*":
        gusto = input("Gusto de la persona: ")
        listaGustos = gustosPersonas.setdefault(nombre, [gusto])
        if listaGustos != [gusto]:
            gustosPersonas[nombre].append(gusto)
        nombre = input("Nombre de la persona: ")
    print(gustosPersonas)
