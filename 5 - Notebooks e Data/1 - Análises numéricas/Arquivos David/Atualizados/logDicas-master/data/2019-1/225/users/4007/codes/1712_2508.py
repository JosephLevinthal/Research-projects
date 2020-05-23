n = int(input("termos: "))

i = 0
p = 3
d1 = 2
d2 = 3
d3 = 4
s = 1
if n == 1:
	print(p)
else:
	while i < (n - 1):
		p = p + (s*(4/(d1*d2*d3)))
		if s == 1:
			s = -1
		else:
			s = 1
		i = i + 1
		d1 = d1 + 2
		d2 = d2 + 2
		d3 = d3 + 2
	print(round(p, 8))