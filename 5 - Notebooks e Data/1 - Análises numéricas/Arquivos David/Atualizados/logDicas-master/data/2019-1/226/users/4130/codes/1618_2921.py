j1 = float(input("Valor do jogo 1: "))
j2 = float(input("Valor do jogo 2: "))

d = 25 / 100

x = j2 - (j2 * d)
total = j1 + x

print(x)
print(round(total, 2))