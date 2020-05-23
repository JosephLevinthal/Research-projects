from math import*
from numpy import*
x = array(eval(input("digite o numero real: ")))
m = sum(x)/size(x)
p = 1
n = size(x)
for i in range(size(x)):
	p = p*(abs(x[i]-m))
p = p**(1/n)
print(round(p,3))