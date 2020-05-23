a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
d = float(input("Valor de d: "))
e = float(input("Valor de e: "))
f = float(input("Valor de f: "))
x = (c * e - b * f)/(a * e - b * d)
y = (a * f - d * c)/(a * e - b * d)

if(x, y >= 0.0):
	print(x)
	print(y)
	
else:
	print("Nao tem solucao")