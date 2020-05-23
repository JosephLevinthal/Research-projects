a = int(input('Numero de habitantes da cidade A: '))
b = int(input('Numero de habitantes da cidade B: '))
c = float(input('Percentual de crescimento da cidade A: '))
d = float(input('Percentual de crescimento da cidade B: '))
c = c/100
d = d/100
f = 0
g = 0
h = 0
while f<=g:
	f = a + a*c
	a = f
	g = b + b*d
	b = g
	h += 1
print(h)