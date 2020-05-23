from numpy import*
from math import*
v = array(eval(input("v: ")))
i = 0
s = 0
while(i < size(v)):
	s = s + v[i]**5
	i = i + 1
a = s / size(v)
b = a ** 0.2
print(round(b, 2))