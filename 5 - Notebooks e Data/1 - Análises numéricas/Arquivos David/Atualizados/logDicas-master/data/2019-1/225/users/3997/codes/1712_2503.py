x = int(input(""))
p = 4
cont = 1
u = 1
m = 1
while cont < x:
	u = u + 2
	m = m*(-1)
	p = p + (4*m)/u
	cont = cont + 1
print(round(p, 8))