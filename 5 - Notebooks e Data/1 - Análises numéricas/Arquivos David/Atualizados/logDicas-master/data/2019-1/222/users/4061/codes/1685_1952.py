salario = float(input("digite salario bruto:"))

if(salario <= 1659.38):
	contribuicao = salario - (salario * 0.08)
elif(salario >= 1659.39 and salario <= 2765.66):
	contribuicao = salario - (salario * 0.09)
elif(salario >= 2765.67 and salario <= 5531.31 ):
	contribuicao = salario - (salario * 0.11)
elif(salario > 5531.31 ):
	contribuicao = salario - 608.44

if(contribuicao <= 1903.98):
	ir = 0
elif(contribuicao >= 1903.99 and contribuicao <= 2826.65):
	ir = contribuicao * 0.075
elif(contribuicao >= 2826.66 and contribuicao <= 3751.05):
	ir = contribuicao * 0.15
elif(contribuicao >= 3751.06 and contribuicao <= 4664.68):
	ir = contribuicao * 0.225
elif(contribuicao > 4664.68):
	ir = contribuicao * 0.275

liquido = contribuicao - ir

print("Salario liquido = R$ " ,(round(liquido, 2)))