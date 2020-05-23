from numpy import *
a = array(eval(input('notas: ')))
b = array(eval(input('nomes: ')))
i = 0
j = 0
f = 0
apr = 0

while a[i] != max(a):
	i += 1
	
while j<size(a):
	if a[j] == -1:
		f =  1
	elif a[j]>=6:
		apr += 1
	j += 1
print(f)
print(apr)
print(size(a)-(apr+f))
j = 0
k = 0
med = 0
while j <size(a):
	if a[j] != -1:
		med += a[j]
		k += 1
	j += 1
print(round(med/k,2))
print(b[i])