from numpy import*
v = array(eval(input()))
i = 7
b = 0 
n = 0
z = 1/i
while b < size(v):
	m = v[b]**i
	i += 0
	b += 1
	n +=m
x = (n/b)**z
print(round(x,2))
