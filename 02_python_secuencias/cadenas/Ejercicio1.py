#! /usr/bin/env python

if __name__ == '__main__':
    cadena = input("Introduce una cadena: ")
    lista = cadena.split(" ")
    acronimo = ""

    # Apartado A
    for palabra in lista:
        acronimo = acronimo + palabra[0].upper()
    print(acronimo)

    # Apartado B
    cadenaCapitalizada = cadena.title()
    print(cadenaCapitalizada)

    # Apartado C
    for palabra in lista:
        if palabra.startswith("a") or palabra.startswith("A"):
            print(palabra, end=" ")
