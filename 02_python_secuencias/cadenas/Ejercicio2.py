#! /usr/bin/env python

if __name__ == '__main__':
    cadena1 = input("Introduce una cadena: ")
    cadena2 = input("Introduce otra cadena: ")
    print()
    if cadena1.find(cadena2) > -1:
        print("cadena2 es subcadena")
    elif cadena2.find(cadena1) > -1:
        print("cadena2 no es subcadena")
    else:
        print(cadena1, "no tiene nada que ver con", cadena2)

    print(cadena1 if cadena1 < cadena2 else cadena2)
