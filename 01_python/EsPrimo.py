def esPrimo(n):
    if n < 1:
        print("1 no es primo")
    elif n == 2:
        print("2 es primo")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(n, "es primo")
        print(n, "es primo")


numero = int(input("Dime un número: "))
esPrimo(numero)
