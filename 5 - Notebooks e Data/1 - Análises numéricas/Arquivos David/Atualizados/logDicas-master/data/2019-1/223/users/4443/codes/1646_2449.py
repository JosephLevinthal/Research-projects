#Valores dos coeficientes
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))
d = float(input("digite o valor de d: "))
e = float(input("digite o valor de e: "))
f = float(input("digite o valor de f: "))

nx = (c*e - b*f)
ny = (a*f - c*d)
d = (a*e - b*d)

if(d == 0):
	print("Nao tem solucao")

else:
	print(nx/d)
	print(ny/d)
	