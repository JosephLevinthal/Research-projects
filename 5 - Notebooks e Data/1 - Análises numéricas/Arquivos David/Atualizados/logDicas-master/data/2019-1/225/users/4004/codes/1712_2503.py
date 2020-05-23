n = int(input("numero de termos: "))

c = 0  #contador
d = 1  #denominador
s = 1  #sinal
p = 0  #pi

while c < n:
	p = p + (s * (4 / d))
	if s == 1:
		s = -1
	else:
		s = 1
	c = c + 1
	d = d + 2
print(round(p, 8))