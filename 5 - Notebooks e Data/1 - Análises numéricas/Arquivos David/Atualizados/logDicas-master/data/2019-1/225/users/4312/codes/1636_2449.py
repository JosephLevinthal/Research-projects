a = float(input("Informe o valor da incognita 'A':\n"))
b = float(input("Informe o valor da incognita 'B':\n"))
c = float(input("Informe o valor da incognita 'C':\n"))
d = float(input("Informe o valor da incognita 'D':\n"))
e = float(input("Informe o valor da incognita 'E':\n"))
f = float(input("Informe o valor da incognita 'F':\n"))

z = (a*e - b*d)

if (z != 0):
	x = (c*e - b*f)/(a*e - b*d)
	y = (a*f - c*d)/(a*e - b*d)	
	print(x)
	print(y)
else:
	print("Nao tem solucao")