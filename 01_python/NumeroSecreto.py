#! /usr/bin/env python
import os

NUM_SECRETO = int(input("Introduce el numero secreto: "))
os.system('cls')

num = int

while num != NUM_SECRETO:
    num = int(input("Introduce un numero: "))
    if num < NUM_SECRETO:
        print("El número introducido es menor que el número secreto")
    elif num > NUM_SECRETO:
        print("El número introducido es mayor que el número secreto")
    else:
        print("Has acertado el número secreto, era ", NUM_SECRETO)
