from numpy import*
from math import*

x = array(eval(input()))

n = size(x)
m = sum(x) / n
s = 0

for i in x:
	s = s + ((i - m) ** 2)

d = sqrt(s / (n - 1))
print(round(d, 3))