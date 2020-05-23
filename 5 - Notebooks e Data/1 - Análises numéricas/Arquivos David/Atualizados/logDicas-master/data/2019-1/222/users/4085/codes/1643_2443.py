# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("escreva o valor do raio do tanque: "))
x = float(input("escreva o valor da altura da coluna de ar: "))
opcao = input("Escreva a opcao desejada? (1/2): ")
a = pi * x**2
b = 3 * r - x
vc = a * b/3
c = 4 * pi
d = r ** 3
vt = c * d/3
e = vt - vc
if (opcao == "1"):
	mensagem = vc
else:
	mensagem = e

print(round(mensagem, 4))
