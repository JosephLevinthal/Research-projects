n = int(input("Quantidade de termos: "))
c = 0
i = 1
e = 0
f = 0
y = 0

while (n - 1 >= c):
	x = (-1)**f/(i*3**e)
	y = (12**(1/2)) * x + y
	c = c + 1
	i = i + 2
	e = e + 1
	f = f + 1
	
print(round(y, 8))	