num = int(input("Numero de 4 digitos: "))
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10
digv = (d1 * 5 + d2 * 4 + d3 * 3 + d4 * 2) % 11
print(digv)