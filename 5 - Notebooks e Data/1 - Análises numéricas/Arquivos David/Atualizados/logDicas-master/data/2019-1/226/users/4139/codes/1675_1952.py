s = float(input("Salario Bruto:"))

if(s <= 1659.38):
	a = s-(s*0.08)
elif(s > 1659.38) and (s <= 2765.66):
	a = s-(s*0.09)
elif(s > 2765.66) and (s <= 5531.31):
	a = s-(s*0.11)
elif(s > 5531.31):
	a = s-608.44


if(a<=1903.98):
	print("Salario liquido = R$",round(a,2))
elif(a > 1903.98) and (a <= 2826.65):
	b = a-(a*0.075)
	print("Salario liquido = R$",round(b,2))
elif(a > 2826.65) and (a <= 3751.05):
	b = a-(a*0.15)
	print("Salario liquido = R$",round(b,2))
elif(a > 3751.05) and (a <= 4664.68):
	b = a-(a*0.225)
	print("Salario liquido = R$",round(b,2))
elif(a > 4664.68):
	b = a-(a*0.275)
	print("Salario liquido = R$",round(b,2))