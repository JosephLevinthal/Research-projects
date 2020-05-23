j1 = float(input("preco do primeiro jogo: "))
j2 = float(input("preco do segundo jogo: "))
d = 0.25
t2 = j2 - (j2 * d)
t1 = j1 + t2
print(round(t2, 2))
print(round(t1, 2))