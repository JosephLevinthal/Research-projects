n = int( input("repeticao: "))
m = 1
o = 3
i = 1
p = 0
q = 0
while (m < n):
	if (n > 1):
		a = ((-1)**(i +1)) * (4 / ((q + 2) * (q + 3) * (q + 4)))
	else:
		p = n
	m = m + 1
	i = i + 1
	q = q + 2
	p = p + a
print(round(p + o, 8))