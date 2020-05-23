from numpy import *
a = array(eval(input('fala meu bom: ')))
b = array(eval(input('fala meu bom: ')))
i = 1
j = 1
v = zeros(12)
while i <13:
	v[i-1] = a[i-1]/100 - b[i-1]/100
	i += 1
i = 0
while v[i] != max(v):
	i += 1
print( i + 1)