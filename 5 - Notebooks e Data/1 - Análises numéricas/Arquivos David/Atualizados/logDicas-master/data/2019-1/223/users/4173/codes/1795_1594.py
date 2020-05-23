from numpy import*
a = array(eval(input()))
p = 1
i = 0
b = 0
while i < size(a):
	dano = a[i]*p
	b += dano
	p += 1
	i += 1
print(b)