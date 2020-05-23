from numpy import*
from math import*

x = array(eval(input()))

n = size(x)
m = sum(x) / n
s = 1

for i in x:
	s = s * abs(i - m)

p = s ** (1 / n)
print(round(p, 3))