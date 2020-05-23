from numpy import *

x = array(eval(input("valores de x: ")))
m = sum(x)/size(x)
a = 0

for g in x:
	a += (g - m)**2
	h = a / (size(x) - 1)
	v = sqrt(h)

print(round(v,3))