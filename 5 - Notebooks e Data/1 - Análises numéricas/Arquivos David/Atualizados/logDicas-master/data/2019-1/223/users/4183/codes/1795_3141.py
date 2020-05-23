from numpy import *
v = array(eval(input("Digite: ")))
cont = 0
while (cont < size(v)):
	m = v[cont]
	m1 = m * 1/6
	cont = cont + 1
	M = (sum(m1)/size(v))**6
print(round(M,2))
	