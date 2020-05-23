d1 = int(input("dado A:"))
d2 = int(input("dado B:"))
r = int(input("rodadas:"))

if ((d1 > 6) or (d1 < 1) or (d2 <1) or (d2 > 6)):
	d ="Entrada invalida"
	print(d)
elif (d1 + d2 == 12):
	a = "CONSTRICAO"
	d = d1+d2+1
	print(a)
	print(d)
elif (d1 + d2 <5):
	a = "POLEN"
	d = (d1+d2+1)*r
	print(a)
	print(d)
elif (d1 + d2 >= 5):
	a = "FRAQUEZA"
	d = d1*d2
	print(a)
	print(d)

