a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))
d = float(input("Digite um numero: "))
e = float(input("Digite um numero: "))
f = float(input("Digite um numero: "))

g = (c*e) - (b*f)
h = (a*e) - (b*d)
i = (a*f) - (c*d)

if h != 0 :
	x = g/h
	y = i/h
	print(x)
	print(y)
else:
	print("Nao tem solucao")