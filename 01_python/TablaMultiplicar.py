#! /usr/bin/env python
print("Tabla de multiplicar Iván Coello")
print()
numero = int(input("Tabla de multiplicar del numero: "))
print()
for f in range(1, 11):
    multiplicacion = numero * f
    print(numero, "x", f, "=", multiplicacion)
