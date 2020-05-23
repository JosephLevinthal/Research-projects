a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
d = float(input("Digite d: "))
e = float(input("Digite e: "))
f = float(input("Digite f: "))

z1 = ((a * e) - (b * d))

if(z1 == 0):
	print("Nao tem solucao")
else:
	print(((c * e) - (b * f)) / z1)
	print(((a * f) - (c * d)) / ((a * e) - (b * d)))