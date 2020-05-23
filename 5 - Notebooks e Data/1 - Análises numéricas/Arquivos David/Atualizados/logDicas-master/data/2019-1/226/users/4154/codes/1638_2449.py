a = float(input("digite um numero: "))
b = float(input("digite um numero: "))
c = float(input("digite um numero: "))
d = float(input("digite um numero: "))
e = float(input("digite um numero: "))
f = float(input("digite um numero: "))

if a*e-b*d == 0:
	print("Nao tem solucao")
else:
	print((c*e-b*f)/(a*e-b*d))
	print((a*f-c*d)/(a*e-b*d))