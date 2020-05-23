preco = float(input("Digite um numero:"))
pgmto = float(input("Digite um numero:"))
X = preco - pgmto
Y = pgmto - preco

if (preco > pgmto):
	print("Falta", X)
else: 
	print("Troco de", Y) 
