#! /usr/bin/env python

if __name__ == '__main__':
    cadena = input("Cadena:")
    if cadena.lower() == cadena[::-1].lower():
        print(cadena, "es un palindromo")
    else:
        print(cadena, "no es un palindromo")
