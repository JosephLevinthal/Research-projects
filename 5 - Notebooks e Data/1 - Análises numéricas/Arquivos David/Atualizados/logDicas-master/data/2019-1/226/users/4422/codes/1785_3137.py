from numpy import *
v = array(eval(input("numeros reais: ")))
t = size(v)
i = 1

while(i<t):
	m = log((exp(v[0]) + exp(v[i]) + exp(v[i + 1]))/exp(t))
	i = i + 1
	print(round(m, 2))
	
	