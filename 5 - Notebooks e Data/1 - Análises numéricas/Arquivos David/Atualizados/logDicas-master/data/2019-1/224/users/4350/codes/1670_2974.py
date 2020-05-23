a = float(input("quantidade de acai em gramas"))
b = float(input("quantidade de salgados"))
c = float(input("valor pago"))
v = (a*24/1000)+(b*3)
if c>v:
	print(round(v, 2))
	print("Sim")
else:
	print(round(v , 2))
	print("Nao")