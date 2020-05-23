from numpy import*
v = array(eval(input("vetor de n numeros:")))
i = 1

while(i >= size(v) - 1):
	m = (v[0] * v[i])**1/2 
	i = i + 1
	print(round(m,2))