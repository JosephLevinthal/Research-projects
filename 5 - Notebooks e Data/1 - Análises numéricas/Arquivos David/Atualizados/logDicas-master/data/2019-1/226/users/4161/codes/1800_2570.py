from numpy import*
from math import*
v = array(eval(input("a parada ai de novo: ")))
p = 1
m = sum(v)/size(v)
n = size(v)
for x in v:
	p = p*abs(x - m)
p = p**(1/n)
print(round(p , 3))