valor=float(input("entre com o valor da compra: "))

if(valor>=200):

	valor_pago=(valor-( valor*5/100))
	print(round(valor_pago,2))
	
else:
	
	print(round(valor,2))