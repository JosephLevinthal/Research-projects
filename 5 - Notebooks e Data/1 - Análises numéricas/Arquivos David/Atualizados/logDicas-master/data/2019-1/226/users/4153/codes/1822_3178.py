from numpy import *

v = array(eval(input("Insira um vetor de inteiros: ")))
# Componentes
n = size(v) 
x = zeros(n, dtype=int)
t = size(v) - 1
r = 0
# Operacao
for i in range(size(v)):
	if(v[i] == 0):
		x[t] = v[i]
		t = t - 1
	elif(v[i]!= 0):
		x[r] = v[i]
		r = r + 1
print(x)