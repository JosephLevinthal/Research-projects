# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

H = float(input('Digite a altura total do tanque: '))
h = float(input('Digite o nivel de combustivel do tanque: '))
r = float(input('Digite o raio dos bojos: '))
print('Entradas:', H,',', h, ',', r)

if (H>0 and h>0 and r>0 and H>h and H>2*r):
	VC = pi*(r**2)*H
	VE = (4/3)*pi*(r**3)
	VK = (pi/3)*(H**2)8