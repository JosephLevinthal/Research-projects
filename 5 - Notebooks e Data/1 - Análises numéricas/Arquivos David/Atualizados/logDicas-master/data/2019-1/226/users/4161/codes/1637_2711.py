dinheiro = float(input("dinheiro: "))
a = int(input("quantos tickets: "))
b = float(input("preco dos tickets: "))
c = int(input("passes de onibus: "))
d = float(input("preco dos passes de onibus: "))
if (dinheiro >= (a*b) + (c*d)):
	print("SUFICIENTE")
else: 
	print("INSUFICIENTE")