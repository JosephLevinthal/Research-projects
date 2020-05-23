from numpy import *
from math import *

x = array(eval(input("digite: ")))

m = sum(x)/size(x)

p = 1
n = size(x)

for i in x:
	p = p *abs(i - m)
p = p**(1/n)
print(round(p, 3))


