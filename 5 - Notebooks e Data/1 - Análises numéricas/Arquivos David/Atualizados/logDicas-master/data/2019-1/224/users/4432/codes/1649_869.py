preco=float(input("digite o preco sem descontos:    "))
if(preco>=200):
	x=preco-preco*0.05
	print(round(x,2))
else:
	print(round(preco,2))
