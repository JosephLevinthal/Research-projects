from numpy import *
a = array(eval(input('vetor de notas: ')))
b = arange(size(a)+1)
i = 0
j = 0
while i < size(a):
	j += a[i]*b[i+1]
	i += 1
print(round(j/sum(b),2))