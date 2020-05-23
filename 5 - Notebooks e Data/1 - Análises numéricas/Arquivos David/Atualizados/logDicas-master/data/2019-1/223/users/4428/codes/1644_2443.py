# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

r = float(input("Digite o valor do raio: ")) 
x = float(input("Digite a altura da coluna de ar: "))
opcao = int(input("Digite a opcao desejada: "))

from math import*
Vt = (pi/3)*(x**2)*(3*r-x)

if(opcao == 1):
	V = Vt

else:
	V = ((4/3*pi*(r**3))-Vt)
	
print(round(V, 4))