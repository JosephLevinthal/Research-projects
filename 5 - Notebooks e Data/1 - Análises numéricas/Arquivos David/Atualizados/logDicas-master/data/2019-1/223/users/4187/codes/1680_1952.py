salarioBruto = float(input("digite o salario bruto do funcionario:"))

#desconto previdenciario
if(salarioBruto <= 1659.38):
	desPrev = salarioBruto *(8/100)
elif(salarioBruto >= 1659.39  and salarioBruto <= 2765.66 ):
	desPrev = salarioBruto *(9/100)
elif(salarioBruto >= 2765.67 and salarioBruto <= 5531.31):
	desPrev = salarioBruto * (11/100)
elif(salarioBruto > 5531.31):
	desPrev = 608.44

#deconto de inposto de renda
salario = salarioBruto - desPrev  
if(salario <= 1903.98):
	desIP = 0
elif(salario >= 1903.99 and salario <= 2826.65):
	desIP = salario * (7.5/100)
elif(salario >= 2826.66 and salario <= 3751.05):
	desIP = salrio * (15/100)
elif(salario >= 3751.06 and  salario <= 4664,68):
	desIP = salario * (22.5/100)
elif(salario > 4664.68):
	desIP = salario * (27.5/100)
	
salario_Liquido = salario - desIP
print("Salario liquido = R$ ",round(salario_Liquido,2))
	
