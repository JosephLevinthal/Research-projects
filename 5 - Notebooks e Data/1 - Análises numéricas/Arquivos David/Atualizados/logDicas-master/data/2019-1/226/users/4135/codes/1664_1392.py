consumo = float(input("Digite o consumo de agua:"))
if (consumo<=10):
	valor = (30+consumo*3)
else:
	valor = (30+consumo*3.5)
print (round(valor,2))	