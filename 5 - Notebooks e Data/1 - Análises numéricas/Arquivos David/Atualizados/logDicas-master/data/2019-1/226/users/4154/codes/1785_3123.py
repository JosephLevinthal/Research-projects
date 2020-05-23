from numpy import *
a = array(eval(input('numeros positivos: ')))
i = 0 
j = 0
while i < size(a):
	j += a[i]**(-1)
	i += 1
print(round((j/size(a))**-1,2))