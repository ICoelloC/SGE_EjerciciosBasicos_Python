print("Ejercicio lista invertida")
lista = ["hola", "mundo", "esto", "es", "prueba"]
listaInvertida = reversed(lista)
for valor in lista:
    print(valor, end=" ")
print()
for valor in listaInvertida:
    print(valor, end=" ")
