
preco=float(input("preco"))
h=preco*5/100
desconto=preco-h
if(preco >= 200.00) :
	print(round(desconto,2))
else :
	print(round(preco,2))
