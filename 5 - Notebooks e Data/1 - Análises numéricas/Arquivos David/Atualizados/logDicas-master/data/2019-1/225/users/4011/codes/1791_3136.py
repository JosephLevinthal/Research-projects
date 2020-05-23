from numpy import*
from math import*

v = array(eval(input("Valores: ")))

i = 0
num = 0
n = size(v)

while(i < size(v)):
	
	num = num + log(v[i] + 1)
	i = i + 1
	
M = exp(num/n) - 1

print(round(M, 2))

