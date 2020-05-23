a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if ((a*e)-(b*d)) == 0:
	print("Nao tem solucao")
else:
	u = (c*e) - (b*f)
	q = (a*f) - (c*d)
	r = (a*e) - (b*d)
	x = u/r
	y = q/r
	print(x)
	print(y)











