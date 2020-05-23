n = int(input("Quantidade de termos: "))
c = 0
i = 1
f = 0
y = 0

while (c <= n - 1):
	y = ((-1)**f) * 4/i + y
	c = c + 1
	i = i + 2
	f = f + 1
	
print(round(y, 8))	