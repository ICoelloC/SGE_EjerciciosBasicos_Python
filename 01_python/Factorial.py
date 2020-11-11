#! /usr/bin/env python
def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = n * factorial(n - 1)
    return resultado


numero = int(input("Dime un numero para calcular su factorial: "))
print(factorial(numero))
