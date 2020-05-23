j1 = float(input("jogo 1: "))
j2 = float(input("jogo 2: "))

des = 25 / 100
#valor do 2 jogo com desconto
j2d = j2 - (j2 * des)

#valor total
total = j1 + j2d

print(round(j2d, 2))
print(round(total, 2))