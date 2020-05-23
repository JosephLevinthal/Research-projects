Saque = int(input('Valor do saque: '))

Notas_100 = Saque//100
resto_100 = Saque%100
Notas_50 = resto_100//50
resto_50 = resto_100%50
Notas_10 = resto_50//10


print(Notas_100)
print(Notas_50)
print(Notas_10)