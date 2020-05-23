valor=float(input("digite o valor da compra:"))
if(valor>= 200):
	desconto=valor-valor*5/100
	print(round(desconto,2))
else:
	sem_desconto=valor
	print(sem_desconto)
	