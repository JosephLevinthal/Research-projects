n = int(input("numero de termos: "))  #quantidade de termos

p = 3    #valor pi
d1 = 2   #denominador 1
d2 = 3   #denominador 2
d3 = 4   #denominador 3
s = 1    #sinal
c = 0    #contador

if n == 1:
	print(p)
else:
	while c < (n - 1):
		p = p + ( s * ( 4 / (d1 * d2 * d3)))
		if s == 1:
			s = -1
		else:
			s = 1
		c = c + 1
		d1 = d1 + 2
		d2 = d2 + 2
		d3 = d3 + 2
	print(round(p, 8))