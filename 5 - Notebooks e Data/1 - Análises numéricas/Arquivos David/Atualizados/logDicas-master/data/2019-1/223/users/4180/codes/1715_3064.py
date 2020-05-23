nome = input("AAMEUL OU HETHRADIAH OU RAKSHASA?")
Valor1 = int(input("Valor do dado 1: "))
Valor2 = int(input("Valor do dado 2: "))
if (Valor1 + Valor2 <= 1):
	print("Entrada invalida")
if(nome == "AAMEUL"):
	if(Valor1 + Valor2 >= 2)or(Valor1 + Valor2 <= 20):
		print(int(Valor1 + Valor2 + 8))
elif(nome == "RAKSHASA"):
	if(Valor1 + Valor2 >= 2)or(Valor1 + Valor2 <= 20):
		print(int(Valor1 + Valor2 + 10))
elif(nome == "HETHRADIAH"):
	if(Valor1 + Valor2 >= 2)or(Valor1 + Valor2 <= 20):
		print(int(Valor1 + Valor2) * 2)
		
		
	

	