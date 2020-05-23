n = int(input())

s = 1
c = 1

while(c < n + 1):
	c2 = 1
	c3 = 3
	numerador = 1
	denominador = 3
	while(c2 < c):
		numerador = numerador * (c2 + 1)
		denominador = denominador * (c3 + 2)
		c2 = c2 + 1
		c3 = c3 + 2
	
	s = s + (numerador / denominador)
	c = c + 1

print(round(s * 2, 10))