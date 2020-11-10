print("======================= BUSCAR, SUSTITUIR, BORRAR =======================")

lista = ["Hola", "Mundo", "esto", "es", "Python", "me", "llamo", "Ivan", "esto", "es", "una", "lista"]

print(lista)

valor = input("¿Qué valor quieres buscar?: ")

if valor in lista:
    print(valor, " aparece ", lista.count(valor), " veces")
else:
    print("No existe el valor", valor, "en la lista")
print()
print(lista)

print()
print()

valorSustituto = input("¿Por qué valor quiere sustituir?: ")
listaTemporal = []
for elemento in lista:
    if elemento == valor:
        elemento = valorSustituto
    listaTemporal.append(elemento)
lista = listaTemporal
print(lista)

print()
print()

valor = input("¿Qué valor quieres borrar?: ")
for elemento in lista:
    if elemento == valor:
        lista.remove(elemento)
print(lista)
