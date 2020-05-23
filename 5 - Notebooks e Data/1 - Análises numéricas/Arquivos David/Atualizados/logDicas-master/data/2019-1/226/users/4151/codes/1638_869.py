x=float(input("preco sem desconto: "))

if(x>=200):
	print(round(x-(x*0.05),2))
else:
	print(x)