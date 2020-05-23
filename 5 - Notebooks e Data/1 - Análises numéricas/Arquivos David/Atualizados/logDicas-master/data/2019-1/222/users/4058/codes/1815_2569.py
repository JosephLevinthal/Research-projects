from numpy import *
from math import *
x = array(eval(input("Numeros: ")), dtype=float)
s = size(x)
m = sum(x)/s
t = 0

for i in x:
	e = (i - m)**2
	t = t + e
	
d = sqrt(t/(s-1))

print(round(d,3))