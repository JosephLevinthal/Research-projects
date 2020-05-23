sbruto = float(input("escreva o salario bruto do funcionario: "))

if (sbruto <= 1659.38):
	sbase = sbruto - (0.08 * sbruto)
	
elif ((sbruto >= 1659.39) and (sbruto <= 2765.66)):
	sbase = sbruto - (0.09 * sbruto)
	
elif ((sbruto >= 2765.67) and (sbruto <= 5531.31)):
	sbase = sbruto - (0.11 * sbruto)
	
elif (sbruto > 5531.31):
	sbase = sbruto - 608.44
	
elif (sbase <= 1903.98):
	sliq = sbase
	print ("Salario liquido = R$", round(sliq, 2))
elif ((sbase >= 1903.99) and (sbase <= 2826.65)):
	sliq = sbase - (0.075 * sbase)
	print ("Salario liquido = R$", round(sliq, 2))
elif ((sbase >= 2826.66) and (sbase <= 3751.06)):
	sliq = sbase - (0.15 * sbase)
	print ("Salario liquido = R$", round(sliq, 2))
elif ((sbase >= 3751.06) and (sbase <= 4664.68)):
	sliq = sbase - (0.225 * sbase)
	print ("Salario liquido = R$", round(sliq, 2))
else:
	sliq = sbase - (0.275 * sbase)
	print ("Salario liquido = R$", round(sliq, 2))

print("Salario liquido = R$", round(sliq, 2))

	
	