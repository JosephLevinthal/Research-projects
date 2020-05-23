a = float(input("variavel: "))
b = float(input("variavel: "))
c = float(input("variavel: "))
d = float(input("variavel: "))
e = float(input("variavel: "))
f = float(input("variavel: "))
lim = a*e-b*d
if(lim!=0):
	x = (c*e-b*f)/lim
	y = (a*f-c*d)/lim
	print(x)
	print(y)
else:
	print("Nao tem solucao")