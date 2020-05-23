from math import*
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input("raio da circuferencia: "))
x= float(input("altura da circuferencia: "))
n = float(input("numero da opcao: "))
ve = 4*(pi*r**3)/3
vc = (pi*x**2)*(3*r-x)/3
if(n==1):
	
	
	v = vc
	
else:
	
	v = ve - vc
print(round(v,4))