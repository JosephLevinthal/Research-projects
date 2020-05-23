from numpy import*

v = array(eval(input("Digite as notas: ")))

i = 0

while( i < size(v)):
	v[i] = v[i] ** 0.5
	i = i + 1



print(round((sum(v)/size(v))**2,2))