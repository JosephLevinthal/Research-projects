nA = int(input("Digite um numero de quatro digitos: "))

nB = nA // 1000
nC = nA // 100 - (nB * 10)
nD = nA // 10 - (nA // 100) * 10
nE = nA % 10

x = (5 * nB + 4 * nC + 3 * nD + 2 * nE) % 11

print(x)