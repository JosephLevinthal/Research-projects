a = float(input("insira a coordenanda a: "))
b = float(input("insira a coordenanda b: "))
c = float(input("insira a coordenanda c: "))
d = float(input("insira a coordenanda d: "))
e = float(input("insira a coordenanda e: "))
f = float(input("insira a coordenanda f: "))
if ((a * e) - (b * d) != 0 ):
	x = (c * e) - (b * f)
	y = (a * f) - (c * d) 
	z = (a * e) - (b * d)
	x1 = x/z
	y1 = y/z
	mensagem = print(x1)
	print(y1)
else:
	mensagem = print("Nao tem solucao")