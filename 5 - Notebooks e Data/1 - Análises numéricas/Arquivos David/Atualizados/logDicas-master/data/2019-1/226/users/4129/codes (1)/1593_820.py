saque = float(input('Valor do saque:'))

notas_50 = saque//50
resto_50 = saque%50

notas_10 = resto_50//10
resto_10 = resto_50%10

notas_2 = resto_10//2

print(int(notas_50))
print(int(notas_10))
print(int(notas_2))
