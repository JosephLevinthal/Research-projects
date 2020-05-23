n = int(input(""))
cont = 1
i = 3
q = 1
p = 12**(1/2)
w = 1
while cont < n:
	q = q*(-1)
	p = p + ((12**(1/2))/(i*(3**w)))*q
	cont = cont + 1
	w = w + 1
	i = i + 2
print(round(p, 8))