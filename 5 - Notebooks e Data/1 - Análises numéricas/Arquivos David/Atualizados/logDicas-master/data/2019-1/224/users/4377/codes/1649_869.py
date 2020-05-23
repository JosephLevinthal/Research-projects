preco=float(input("p"))
w=preco*5/100
desconto=preco-w
if(preco>=200.00):
	print(round(desconto,2))
else:
	print(round(preco,2))