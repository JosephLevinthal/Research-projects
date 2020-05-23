a = float(input("Insira valor de a: "))
b = float(input("Insira valor de b: "))
c = float(input("Insira valor de c: "))
d = float(input("Insira valor de d: "))
e = float(input("Insira valor de e: "))
f = float(input("Insira valor de f: "))


if((a * e) - (b * d) != 0):
	x = ((c * e) - (b * f))/((a * e) - (b * d))
	y = ((a * f) - (c * d))/((a * e) - (b * d))
	print(x)
	print(y)
else:
	msg = "Nao tem solucao"
	print(msg)