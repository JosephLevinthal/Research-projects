from numpy import *

P = array(eval(input('')))
A = array(eval(input('')))
V = zeros(size(P))

for i in range(size(P)):
	V[i] = round((P[i])/((A[i])*(A[i])), 2)
print(V)
	
m = max(V)
print('O MAIOR IMC DA TURMA EH: ',m)

if (m<17):
	print('MUITO ABAIXO DO PESO')
if (17<=m<=18.49):
	print('ABAIXO DO PESO')
if (18.5<=m<=24.99):
	print('PESO NORMAL')
if (25<=m<=29.99):
	print('ACIMA DO PESO')
if (30<=m<=34.99):
	print('OBESIDADE')
if (35<=m<=39.99):
	print('OBESIDADE SEVERA')
if (m>=40):
	print('OBESIDADE MORBIDA')