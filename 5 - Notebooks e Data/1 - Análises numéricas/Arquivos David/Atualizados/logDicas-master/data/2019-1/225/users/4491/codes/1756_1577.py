from numpy import *

v = array(eval(input("v: ")))
v0 = array(eval(input("v0: ")))
n = array(eval(input("numero int: ")))
t = arange(n)
d = zeros(n)
i = 0

while(i<n):
	d[i] = (v * (t[i]**2) / 2) + v0*t[i]
	i = i + 1
print(d)
