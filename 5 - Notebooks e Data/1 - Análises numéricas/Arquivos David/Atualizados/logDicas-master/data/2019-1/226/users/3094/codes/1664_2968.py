n1 = input("L ou S: ")
ql = float(input("quantidade de lanches ou salgados: "))
qr = float(input("quantidade de refrigerantes: "))
l = 5
s = 3.50
r = 4
if(n1 == "L"):
	pf = ql * 5 + qr * 4
	print(round(pf, 2))
else:
	pf = ql * 3.50 + qr * 4
	print(round(pf, 2))