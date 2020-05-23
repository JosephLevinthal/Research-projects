from numpy import *
a = array(eval(input('notas: ')))
b = array(eval(input('presenca: ')))
c = float(input('carga horaria: '))
d = zeros(3, dtype=int)
for i in range(size(a)):
	if a[i]<5:
		d[1]+= 1 
	elif b[i] < c*0.75:
		d[2] += 1
	elif a[i]>= 5 and b[i]>= c*0.75:
		d[0] += 1
	
print(d)