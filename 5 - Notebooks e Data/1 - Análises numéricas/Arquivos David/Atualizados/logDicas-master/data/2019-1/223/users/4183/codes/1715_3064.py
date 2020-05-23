cab = input("Cabeca: ")
d1 = int(input("Numero: "))
d2 = int(input("Numero: "))

if(0 < d1 and d1 < 10) and (0 < d2 and d2 < 10):
	if (cab == "AAMEUL"):
		print(8 + (d1 + d2))
	elif (cab == "HETHRADIAH"):
		print((d1 + d2)*2)
	elif (cab == "RAKSHASA"):
		print(10 + (d1 + d2))
			
else:
	print("Entrada invalida")
			