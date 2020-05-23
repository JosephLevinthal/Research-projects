from numpy import*
from numpy.linalg import*

a=array(eval(input('digite um numero: ')))
alimentos=array([[2, 1, 4 ], [1, 2, 0 ], [2, 3, 2 ]])
a = a.T

b = dot(inv(alimentos), a)

print('estafilococo:', round(b[0],1))
print('salmonela:', round(b[1],1))
print('coli:', round(b[2],1))

if b[0]==min(b):
	print('estafilococo')
elif b[1]==min(b):
	print('salmonela')
else:
	print('coli')