from numpy import *

v = array(eval(input("v: ")))

c = 0

for i in range(size(v)):
	c = c + v[i]**(1/6)
m = (c/size(v))**6
print(round(m, 2))