a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
d = float(input("Digite d: "))
e = float(input("Digite e: "))
f = float(input("Digite f: "))


if((a*e - b*d) != 0):
	x = (c*e - b*f)/(a*e - b*d)
	y = (a*f - c*d)/(a*e - b*d)
	print(x)
	print(y)

else:
	print("Nao tem solucao")