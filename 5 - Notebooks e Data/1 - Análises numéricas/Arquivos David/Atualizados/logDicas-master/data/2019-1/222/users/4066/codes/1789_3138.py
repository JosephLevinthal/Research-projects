from numpy import *

v = array(eval(input("Numeros: ")), dtype=float)

t = 0

d = 0

while (t < size(v)):
	d = d + v[t]**7
	
	t = t + 1
	
M = (d/size(v))**(1/7)

print(round(M,2))