cadena1 = input("Introduce una cadena: ")
cadena2 = input("Introduce otra cadena: ")
print()

if cadena2 in cadena1:
    print(cadena2, "es una subcadena de ", cadena1)
elif cadena1 in cadena2:
    print(cadena1, "es una subcadena de ", cadena2)
else:
    print(cadena1, "no tiene nada que ver con", cadena2)

if cadena1 < cadena2:
    print(cadena1)
else:
    print(cadena2)
