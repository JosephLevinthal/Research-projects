
mulher=input("S ou N?")
ingresso=float(input("valoringresso:"))
quantidade=int(input("quantos deseja:"))
valor=ingresso*quantidade
if (mulher=="S"):
	print(round(valor*0.8, 2))
else:
	print(round(valor, 2))
