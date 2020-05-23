opcao = input("C/F?")
if (opcao == "C"):
	C = float(input(" Digite a temperatura "))
	F = (9/5)*C +32
	print(round(F,2))
else:
	F = float(input(" Digite a temperatura "))
	C = 5/9*(F - 32)
	print(round(C,2))
	


	 


