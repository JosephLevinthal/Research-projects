escala= input("C ou F: ")
valor= float(input("Valor da Temperatura: "))

if (escala == "C"):
	formula2=(valor * 1.8)+ 32
	print(round(formula2, 2))
	
else:
	formula= (5/9*(valor - 32))
	print(round(formula, 2))