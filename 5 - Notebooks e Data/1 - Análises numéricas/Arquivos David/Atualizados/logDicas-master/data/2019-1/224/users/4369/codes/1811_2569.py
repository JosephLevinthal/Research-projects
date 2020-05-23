from numpy import*
from math import*
v = array(eval(input("Digite um vet: ")))
m = sum(v) / size(v)
d = sqrt((x[i] - m)** 2) 
for i in range(size(v)):
	print(round(d, 3))