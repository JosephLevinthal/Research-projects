from numpy import *

x = array(eval(input("valores de x: ")))
m = sum(x)/size(x)
a = 1

for g in x:
	a *= abs(g - m)
	h = a
	v = h**(1/size(x))


print(round(v,3))