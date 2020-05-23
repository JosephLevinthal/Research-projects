a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
d = float(input("D: "))
e = float(input("E: "))
f = float(input("F: "))

x1 = (c*e - b*f)
x2 = (a*e - b*d)
y1 = (a*f - c*d)


if (x2 == 0):
	mensagem = "Nao tem solucao"
	print(mensagem)
else:
	X = x1/x2
	print(X)
	Y = y1/x2
	print(Y)
	