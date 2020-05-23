from numpy import *
v = array(eval(input("v: ")))
i = 0
m = 0
n = 0
while(n==m):
	m = (exp(v[i]))/exp(n) + m
	i = i + 1
	n = n + 1
print(round(log(m), 2))