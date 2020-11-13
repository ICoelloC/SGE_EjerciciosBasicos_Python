#! /usr/bin/env python
def generadorprimos(n):
    primos = [2]
    a = 2
    while a < n:
        contador = 0
        for i in primos:
            if a % i == 0:
                contador += 1
        if contador == 0:
            primos.append(a)
        else:
            pass
        a = a + 1
    print(primos)


if __name__ == '__main__':
    generadorprimos(18)
