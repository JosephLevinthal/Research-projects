escala = input("Digite a escala (C/F): ")
temp = float(input("Digite o valor da temperatura: "))
F = (9 *temp)/5 + 32
C = (5 *(temp - 32))/9

if (escala == "C"):
	print(round(F,2))
else: 
	print(round(C,2))
	