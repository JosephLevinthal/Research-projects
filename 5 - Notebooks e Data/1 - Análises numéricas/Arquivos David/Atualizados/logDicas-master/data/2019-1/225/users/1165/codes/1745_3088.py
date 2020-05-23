x = int(input("Leia o numero: "))
c = 0
p = 0
i = 0

while (x!=0):
	if(x == 0):
		p = p+1
	else:
		i = i + 1
	c = c + 1
	x = int(input("Leia o numero: "))
if(p > 0):
	d = p/c
	print(round(d, 2))
elif(i > 0):
	e = i/c
print(round(e, 2))