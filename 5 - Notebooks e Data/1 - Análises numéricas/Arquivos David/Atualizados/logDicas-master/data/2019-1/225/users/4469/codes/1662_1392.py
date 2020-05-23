consumo = float(input("Consumo de agua: "))

if(consumo < 10.0):
	valor_a_pagar = 30.0 + (consumo * 3)
	print(round(valor_a_pagar, 2))
else:
	valor_a_pagar = 30.0 + (consumo * 3.5)
	print(round(valor_a_pagar, 2))