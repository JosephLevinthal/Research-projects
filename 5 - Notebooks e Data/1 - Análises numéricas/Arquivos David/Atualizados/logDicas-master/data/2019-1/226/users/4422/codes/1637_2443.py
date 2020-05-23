# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("Qual o raio? "))
x = float(input("Altura: "))
opcao = int(input("Qual? (1/2)"))
vesf = (4*pi*(r)**3)/3
vcal = (pi*((x)**2)*(3*r - x))/3

if(opcao == 2):
	mens = vesf - vcal
	
else:
	mens = vcal
	
print(round(mens, 4))	