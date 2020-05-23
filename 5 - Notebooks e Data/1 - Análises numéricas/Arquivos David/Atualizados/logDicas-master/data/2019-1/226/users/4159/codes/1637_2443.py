# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input("variavel: "))
h = float(input("variavel: "))
opcao = int(input("escolha:(1/2)"))
from math import*
ve=(4*pi*r**3)/3
vc=((pi*h**2)*(3*r-h))/3
if(opcao == 1):
	print(round(vc, 4))
else:
	print(round(ve-vc, 4))