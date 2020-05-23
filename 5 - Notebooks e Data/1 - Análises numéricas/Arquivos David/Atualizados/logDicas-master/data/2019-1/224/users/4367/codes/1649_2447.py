preco= float(input("digite o preco: "))
pg= float(input("digite o pagamento: "))
x=pg-preco
p=preco-pg
if(preco>pg):
	print(("Falta"),(round(p, 2)))
else:
	print(("Troco de"),(round(x, 2)))