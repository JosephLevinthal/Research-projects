from numpy import *

v = array(eval(input("insira os numeros:")))

m = sum(v)/size(v)
n = size(v)
p = 1

for i in range(size(v)):
	p = p * abs(v[i] - m)
	
print(round(p**(1/n),3))