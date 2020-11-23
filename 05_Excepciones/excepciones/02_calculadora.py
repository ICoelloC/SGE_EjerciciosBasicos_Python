#! /usr/bin/env python

def pedir_opcion():
    correcto = False
    opc = ""
    while not correcto:
        try:
            opc = input("Elige una opción: ")
            correcto = True
        except ValueError:
            print('Error, introduce un carácter')
    return opc


def pedir_valor():
    correcto = False
    val = 0
    while not correcto:
        try:
            val = float(input("Introduce un valor: "))
            correcto = True
        except ValueError:
            print('Error, introduce un valor numérico')
    return val


def pedir_valor_distinto_cero():
    correcto = False
    val = 0
    while not correcto:
        try:
            val = float(input("Introduce un valor: "))
            if val != 0:
                correcto = True
            else:
                print("Introduzca un valor distinto de cero")
        except ValueError:
            print('Error, introduce un valor numérico')
    return val


def sumar(n1, n2):
    print(n1, "+", n2, "=", (n1 + n2))
    print()


def restar(n1, n2):
    print(n1, "-", n2, "=", (n1 - n2))
    print()


def multiplicar(n1, n2):
    print(n1, "x", n2, "=", (n1 * n2))
    print()


def dividir(n1, n2):
    try:
        if n2 == 0:
            raise ZeroDivisionError
        else:
            print(n1, "/", n2, "=", (n1 / n2))
    except ZeroDivisionError:
        print("ERROR: no se puede dividir entre 0")
        n2 = pedir_valor_distinto_cero()
        print(n1, "/", n2, "=", (n1 / n2))
        print()


def potencia(n1, n2):
    print(n1, "^", n2, "=", (n1 ** n2))
    print()


if __name__ == '__main__':
    salir = False
    opcion = ""
    while not salir:
        num1 = pedir_valor()
        num2 = pedir_valor()
        print()
        print("+ Sumar")
        print("- Restar")
        print("* Multiplicar")
        print("/ Dividir")
        print("^ Potencia")
        print("S Salir")
        opcion = pedir_opcion()
        print()
        if opcion == "+":
            sumar(num1, num2)
        elif opcion == "-":
            restar(num1, num2)
        elif opcion == "*":
            multiplicar(num1, num2)
        elif opcion == "/":
            dividir(num1, num2)
        elif opcion == "^":
            potencia(num1, num2)
        elif opcion == "S":
            salir = True
        else:
            print("Introduzca una opción válida")
