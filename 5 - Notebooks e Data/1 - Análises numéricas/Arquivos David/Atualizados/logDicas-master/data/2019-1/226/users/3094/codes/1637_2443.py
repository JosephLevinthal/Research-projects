# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
raio = float(input("raio: "))
altura = float(input("altura: "))
opcao = input("1 ou 2: ")
from math import *
#ve = (4 * pi * (raio ** 3)) / 3
#vc = (pi * (altura ** 2) * (3 * raio - altura)) / 3
if (opcao == "1"):
	sair = (pi * (altura ** 2) * (3 * raio - altura)) / 3
	print(round(sair, 4))
else:
	sair = ((4 * pi * (raio ** 3)) / 3) - ((pi * (altura ** 2) * (3 * raio - altura)) / 3)
	print(round(sair, 4))