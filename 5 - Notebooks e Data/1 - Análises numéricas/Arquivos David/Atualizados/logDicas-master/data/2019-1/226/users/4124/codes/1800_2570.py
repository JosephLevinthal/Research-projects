from numpy import *

v = array(eval(input("Vetor de numeros reais: ")))
m = sum(v)/size(v)
n = size(v)
p = 1
for i in range(n):
	p = p * (abs(v[i]- m))
p = p ** (1/n)
print(round(p,3))
	
	