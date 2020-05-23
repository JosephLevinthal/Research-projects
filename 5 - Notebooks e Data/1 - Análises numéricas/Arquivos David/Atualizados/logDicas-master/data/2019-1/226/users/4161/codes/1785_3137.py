from numpy import*
from math import*
v = array(eval(input("vetor: ")))
n = size(v)
s = sum(v)
t = 0
a = 0
while t<n:
	a = a + exp(v[t])
	t = t + 1
x = a/exp(n)
m = log(x)
print(round(m, 2))
