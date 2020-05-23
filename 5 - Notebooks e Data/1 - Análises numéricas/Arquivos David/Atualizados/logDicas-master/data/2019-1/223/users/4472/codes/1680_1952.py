salarioBruto = float(input("Valor do Salario Bruto: "))


# Cálculo da Contribuição Previdenciaria
if salarioBruto <= 1659.38:
	descontoContribuicao = salarioBruto * (8/100)
	
elif  salarioBruto == 1659.39 and salarioBruto <= 2765.66:
	descontoContribuicao = salarioBruto * (9/100)
	
elif  salarioBruto == 2765.67 and salarioBruto <= 5531.31:
	descontoContribuicao = salarioBruto * (11/100)
elif  salarioBruto > 5531.31:
	descontoContribuicao = 608.44
		
salarioBase = salarioBruto - descontoContribuicao

# Cálculo do Imposto de Renda

if salarioBase <= 1903.98:
	impostoRenda = "Isento"

elif salarioBase == 1903.99 and salarioBase <= 2826.65:
	impostoRenda =  (salarioBruto - contribuicaoPrevidenciaria) - ((salarioBruto - contribuicaoPrevidenciaria) * 7.5 / 100)
	
elif salarioBase == 2826.66 and salarioBase <= 3751.05:
	impostoRenda =  (salarioBruto - contribuicaoPrevidenciaria) - ((salarioBruto - contribuicaoPrevidenciaria) * 15 / 100)

elif salarioBase == 3751.05 and salarioBase <= 4664.68:
	impostoRenda =  (salarioBruto - contribuicaoPrevidenciaria) - ((salarioBruto - contribuicaoPrevidenciaria) * 22.5 / 100)
	
elif salarioBase > 4664.68:
	impostoRenda =  (salarioBruto - contribuicaoPrevidenciaria) - ((salarioBruto - contribuicaoPrevidenciaria) * 27.5 / 100)

#Salario líquido
salarioLiquido = salarioBruto - contribuicaoPrevidenciaria - impostoRenda



print ("Salario liquido = R$".round(salarioLiquido,2))
