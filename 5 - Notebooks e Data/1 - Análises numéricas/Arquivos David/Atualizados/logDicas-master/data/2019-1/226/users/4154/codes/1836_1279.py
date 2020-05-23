from numpy import *
from numpy.linalg import *
a = array(eval(input()))
b = str(input()).lower()
k = 0
j = 0
life = 100
moedas = 0
#c = zeros(len(b), dtype = int)
for i in range(len(b)):
	if b[i] == 'w':
		k -= 1
	elif b[i] == 's':
		k += 1
	elif b[i] == 'a':
		j -= 1
	elif b[i] == 'd':
		j += 1
	if a[k,j] == 11:
		moedas += 1
		a[k,j] = 0
	elif a[k,j] == 22:
		life -= 5
print('posicao x: ',j)
print('posicao y: ',k)
print('moedas: ',moedas)
print('life: ',life)