salario = float(input("Salario bruto: "))

if(salario <= 1659.38):
	d = salario * 0.92
elif(salario >= 1659.39 and salario <= 2765.66):
	d = salario * 0.91
elif(salario >= 2765.67 and salario <= 5531.31):
	d = salario * 0.89
elif(salario > 5531.31):
	d = salario - 608.44
d	
if(d <= 1903.98):
	print("Salario liquido = R$ ",round(d,2))
elif(d >=1903.99 and d <= 2826.65):
	r = d * 0.925
	print("Salario liquido = R$ ",round(r,2))
elif(d >=2826.66 and d <= 3751.05):
	r = d * 0.85
	print("Salario liquido = R$ ",round(r,2))
elif(d >=3751.06 and d <= 4664.68):
	r = d * 0.775
	print("Salario liquido = R$ ",round(r,2))
elif(d > 4664.68):
	r = d * 0.725
	print("Salario liquido = R$ ",round(r,2))
