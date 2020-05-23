# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("Digite o raio: "))
a = float(input("Digite a altura: "))
opcoes = float(input(" Digite o opcao 1 ou 2: ")) # opções de volume de ar ou volume do combustível
vE = (4 * (pi * (r**3))) / 3 # volume da esfera
vA1 = ((pi * (a**2)) * ((3 * r) - a)) / 3 # Volume de ar é igual a volume da calota esférica
vC2 = vE - vA1 #volume do combustível
if(opcoes == 1):
	print(round(vA1, 4))
else:
	print(round(vC2, 4))

