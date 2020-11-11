#! /usr/bin/env python
lista1 = ["Hola", "Mundo", "esto", "es", "Python", ",", "me", "llamo", "Ivan", ",", "y", "esto", "es", "una", "lista"]
lista2 = ["Esta", "es", "otra", "lista", ",", "en", "esta", "lista", "no", "se", "que", "mas", "poner", "en", "ella"]

listaValoresIguales = []
listaValoresDistintos1 = []
listaValoresDistintos2 = []

for i in lista1:
    if i in lista2:
        listaValoresIguales.append(i)
    if i not in lista2:
        listaValoresDistintos1.append(i)

for i in lista2:
    if i not in lista1:
        listaValoresDistintos2.append(i)

print("============= LISTA 1 =============")
print(lista1)
print()
print("============= LISTA 2 =============")
print(lista2)
print()
print("============= LISTA VALORES IGUALES =============")
print(listaValoresIguales)
print()
print("============= LISTA VALORES QUE NO ESTAN EN LA LISTA 2 =============")
print(listaValoresDistintos1)
print()
print("============= LISTA VALORES QUE NO ESTAN EN LA LISTA 1 =============")
print(listaValoresDistintos2)
