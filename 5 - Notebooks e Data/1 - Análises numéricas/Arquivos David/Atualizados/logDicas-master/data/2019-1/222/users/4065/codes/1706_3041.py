x = float(input("valor de x: "))
if(x == -2)  or (x == 2) or ((x < -1000) and (x > -2)) or (x < 2) and (x > 1000):
	print("entrada invalida")
else:
	if(x >= -1000) and (x < -2):
		valor = -((1 ) / (x + 2))
		print(round(valor,4))

	elif(x > 2) and (x <= 1000):
		valor = (1 / (x - 2))
		print(round(valor,4))
	