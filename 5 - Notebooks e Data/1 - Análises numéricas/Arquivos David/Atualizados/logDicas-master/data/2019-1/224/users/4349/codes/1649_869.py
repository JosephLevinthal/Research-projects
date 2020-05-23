entrada= float(input("preco da compra sem desconto: "))
desconto= entrada * 5/100
if (entrada>=200):
	print(round(entrada - desconto, 2))
else:
   print("sem desconto")