a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
d = float(input("digite d: "))
e = float(input("digite e: "))
f = float(input("digite f: "))
denominador = (a*e  - b*d)

if denominador !=  0:
	print((c*e - b*f) / (a*e - b*d))
	print((a*f - c*d) / (a*e - b*d))
else:
	print("Nao tem solucao")
	