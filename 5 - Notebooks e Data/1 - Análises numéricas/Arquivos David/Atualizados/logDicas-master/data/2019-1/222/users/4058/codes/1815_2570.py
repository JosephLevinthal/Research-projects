from numpy import *
from math import *
x = array(eval(input("Numeros: ")), dtype=float)
s = size(x)
m = sum(x)/s
t = 1

for i in x:
	e = abs(i - m)
	t = t*e
	
p = pow(t, (1/s))

print(round(p,3))