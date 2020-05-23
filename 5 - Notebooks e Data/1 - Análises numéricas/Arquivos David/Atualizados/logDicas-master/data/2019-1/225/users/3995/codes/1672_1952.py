x=float(input("salario:"))
#Salário bruto menos alíquota
if(x<=1659.38):
	h=round((x-(x*0.08)),2)
	print("Salario liquido=R$",h)
elif(x>=1659.39)and(x<=2765.66):
	h=round((x-(x*0.09)),2)
	if(h<=1903.98):
		print("Salario liquido=R$",h)
	else:
		y=round((h-(h*0.075)),2)
		print("Salario liquido=R$",y)
elif(x>=2765.67)and(x<=5531.31):
	h=x-(x*0.11)
	if(x<=1903.98):
		print("Salario liquido=R$",h)
	elif(h<=2826.65 and h>=1903.99):
		y=round((h-(h*0.075)),2)
		print("Salario liquido=R$",y)
	elif(h>=2826.66)and(h<=3751.05):
		y=round((h-(h*0.15)),2)
		print("Salario liquido=R$",y)
	elif(h>=3751.06)and(h<=4664.68):
		y=round((h-(h*0.225)),2)
		print("Salario liquido=R$",y)
	else:
		y=round((h-(h*0.275)),2)
		print("Salario liquido=R$",y)
else:
	h=x-608.44
	y=round((h-(h*0.275)),2)
	print("Salario liquido=R$",y)