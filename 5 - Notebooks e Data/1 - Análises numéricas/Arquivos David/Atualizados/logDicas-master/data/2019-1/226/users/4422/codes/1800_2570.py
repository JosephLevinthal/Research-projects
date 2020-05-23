from numpy import *
from math import *
x = array(eval(input("vai: ")))
n = size(x)
i = 1
m = sum(x)/size(x)

for a in x:
	i = i * abs(a - m)
i = i**(1/n)
print(round(i, 3))