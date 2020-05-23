a = int(input('Numero de habitantes A: '))
b = int(input('Numero de habitantes B: '))
x = float(input('Percentual de crescimento A: '))
y = float(input('Percentual de crescimento B: '))

c = 0

while (a<b):
	a = a*(x/100)+a
	b = b*(y/100)+b
	c = c+1
	
print(c)