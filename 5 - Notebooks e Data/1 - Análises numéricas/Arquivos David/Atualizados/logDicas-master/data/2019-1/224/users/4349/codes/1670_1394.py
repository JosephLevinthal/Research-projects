quantidade= float(input("horas: "))

sem= 50*quantidade

if (quantidade<=20):
	x= quantidade*50+70
	print(x)

else:
	pagamento= (quantidade - 20)*50+70*quantidade-5
	print(pagamento)