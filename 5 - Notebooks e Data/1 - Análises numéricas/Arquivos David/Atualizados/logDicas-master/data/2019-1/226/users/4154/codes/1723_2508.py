a = int(input('numero de termos da serie: '))
i = 0
p = 0
h = 0
while i<a-1:
	p += (-1)**i*(4/((2+h)*(3+h)*(4+h)))
	i += 1
	h += 2
print(round(3.0 + p,8))