from numpy import *
a = array(eval(input('nivel de glicose: ')))
i = 0
j = 0

while j < size(a):
	if a[j]>99:
		print(j)
		i += 1
	j+=1
print(i)