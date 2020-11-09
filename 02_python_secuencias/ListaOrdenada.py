# lista = [1, 2, 3, 4]
lista = [4, 1, 3, 2]
lista2 = lista[:]
lista.sort()
if lista == lista2:
    print("Lista ordenada")
else:
    print("Lista no ordenada")
