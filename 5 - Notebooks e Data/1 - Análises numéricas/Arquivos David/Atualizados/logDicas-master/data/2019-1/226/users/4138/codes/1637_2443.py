# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input("insira o raio do tanque: "))
a = float(input("insira a altura do tanque: "))
opcao = input("insira a opcao desejada: (1/2)")
from math import *

Vr = ((4 * pi) * (r**3))
Vr1 = Vr/3

Vra1 = (pi * (a**2))
Vra2 = ((3 * r) - a)
Vrat = (Vra1 * Vra2)/3

Vc = Vr1 - Vrat

if(opcao == "1"):
	mensagem = Vrat
	print(round(Vrat,4))
else:
	mensagem = Vc
	print(round(Vc,4))


