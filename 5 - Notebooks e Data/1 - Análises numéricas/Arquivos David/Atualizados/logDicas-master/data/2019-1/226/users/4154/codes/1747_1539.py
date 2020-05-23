x = float(input('numr'))
k = int(input('numr'))
i = 0
b = 0
while k-1>=i:
	if i%2 == 0:
		a = x**i
	else:
		a = -1*(x**i)
	c = a + b
	b = c
	i += 1
	a = 0
print(round(c,7))