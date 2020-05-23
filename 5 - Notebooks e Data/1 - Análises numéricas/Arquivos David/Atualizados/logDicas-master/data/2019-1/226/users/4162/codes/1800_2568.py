from numpy import*
m = int(input("tamanho:"))
f = zeros(m, dtype=int)
d = "*"
e = "*"
g = ""
o = ""
for i in range(size(f)):
	e = "*"
	d = "*"
	g = g + o
	d = "*"*m
	e = "*"*m
	print(d+o+e)
	m = m - 1
	o = o +"oo"