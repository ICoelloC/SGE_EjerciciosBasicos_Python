print("Conversor de minutos a horas")
minutos = int(input("Introduce los minutos: "))
print()

horas = minutos // 60
minutosRestantes = minutos % 60

print(minutos, "minutos son", horas, "horas, y", minutosRestantes, "minutos")
