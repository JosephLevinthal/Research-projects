#Definição da escala
escala = input("Em que escala a temp esta representada")
temp = float(input("Qual o valor da temperatura? "))

calcc = 5/9*(temp-32)
calcf = (9/5*temp) + 32

if (escala == "F"):
	print(calcc)
	
else:
	print(calcf)
	

