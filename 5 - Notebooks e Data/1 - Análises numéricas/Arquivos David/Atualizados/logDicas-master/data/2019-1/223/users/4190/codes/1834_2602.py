from numpy import *
from numpy.linalg import *

alimento = array([[2, 1, 4], [1, 2, 0], [2, 3, 2]])
quantidade = array(eval(input()))
quantidade = quantidade.T
mg = dot(inv(alimento), quantidade)

print('estafilococo: ', round(mg[0], 1))
print('salmonela: ', round(mg[1], 1))
print('coli: ', round(mg[2], 1))

if mg[0] == min(mg):
	print('estafilococo')
elif mg[1] == min(mg):
	print('salmonela')
else:
	print('coli')