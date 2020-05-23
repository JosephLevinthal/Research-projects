escala = input ("Digite a escala? (C/F):")
temp = float (input("Digite o valor da temperatura:"))
C = 5/9*(temp-32)
F = (9*temp+160)/5
if (escala == "C"):
	print (round(F,2))
else:
	print (round(C,2))