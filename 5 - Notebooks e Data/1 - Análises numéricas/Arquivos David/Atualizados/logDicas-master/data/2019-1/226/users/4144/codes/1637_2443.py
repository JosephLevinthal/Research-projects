# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
raio = float(input("digite o valor do raio: "))
x = float(input("digite o valor da altura: "))
ops = int(input("O numero da opcao desejada: "))
vol = (4 * pi * (raio) ** 3) / 3
calota = (pi * (x) ** 2 * ((3 * raio) - x)) / 3
combs = vol - calota
if (ops == 1):
	print(round(calota,4))
if (ops == 2):
	print(round(combs,4))
