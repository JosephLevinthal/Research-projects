preco = float(input("preo"))
desc = (preco/100*5)
if(preco >= 200):
	print(round(preco - desc,2))
else:
	print(round(preco,2))