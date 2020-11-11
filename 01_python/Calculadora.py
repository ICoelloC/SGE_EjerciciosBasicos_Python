#! /usr/bin/env python
print("Calculadora Iván Coello")

n1 = float(input("Introduce el valor1: "))
n2 = float(input("Introduce el valor2: "))
print()

suma = n1 + n2
print(n1, "+", n2, "=", suma)

resta = n1 - n2
print(n1, "-", n2, "=", resta)

multiplicacion = n1 * n2
print(n1, "x", n2, "=", multiplicacion)

if n2 == 0:
    print("no se puede dividir entre cero")
else:
    division = n1 / n2
    print(n1, "/", n2, "=", division)

potencia1 = n1 ** n2
print(n1, "^", n2, "=", potencia1)

potencia2 = n2 ** n1
print(n2, "^", n1, "=", potencia2)
