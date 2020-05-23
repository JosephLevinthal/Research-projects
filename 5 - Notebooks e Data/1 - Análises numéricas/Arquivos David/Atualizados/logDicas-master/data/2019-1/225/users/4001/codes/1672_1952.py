SB = float(input("Salario bruto: "))
# Desconto da contribuicao previdenciaria
if (SB <= 1659.38):          #Salario bruto
	Sb = SB - (SB * 8/100)    #Salario base eh isento
	print("Salario liquido = R$", round(Sb, 2))
elif (SB >= 1659.39) and(SB <= 2765.66):     #Salario bruto
	Sb = SB - (SB * 9/100)    #Aliquota
	if (Sb <= 1903.98):       #Salario base eh isento
		print("Salario liquido = R$", round(Sb, 2))
	else:
		Sl = Sb - (Sb * 7.5/100)
		print("Salario liquido = R$", round(Sl, 2))
elif (SB >= 2765.67) and (SB <= 5531.31):
	Sb = SB - (SB * 11/100)
	if (Sb <= 2826.65):
		Sl = Sb - (Sb * 7.5/100)
		print("Salario liquido = R$", round(Sl, 2))
	elif (Sb >= 2826.66) and (Sb <= 3751.05): 
		Sl = Sb - (Sb * 15/100)
		print("Salario liquido = R$", round(Sl, 2))
	elif (Sb >= 3751.06) and (Sb <= 4664.68):
		Sl = Sb - (Sb * 22.5/100)
		print("Salario liquido = R$", round(Sl, 2))
	else:
		Sl = Sb - (Sb * 27.5/100)
		print("Salario liquido = R$", round(Sl, 2))
else:
	Sb = SB - 608.44
	Sl = Sb - (Sb * 27.5/100)
	print("Salario liquido = R$", round(Sl, 2))
	
		
		
	
	