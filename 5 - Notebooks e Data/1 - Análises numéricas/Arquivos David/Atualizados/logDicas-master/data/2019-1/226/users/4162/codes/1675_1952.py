sb= float(input("insira o salario bruto: "))
# desconto da contribuiçã previdenciaria
if (sb<=1659.38):
	slp= sb-(sb*0.08)
elif (sb>=1659.39)and(sb<=2765.66):
	slp= sb-(sb*0.09)
elif (sb>=2765.67)and(sb<=5531.31):
	slp= sb-(sb*0.11)
elif (sb>5531.31):
	slp= sb-608.44
# desconto do imposto de renda
if (slp<=1903.98):
	sl=slp
elif (slp>=1903.99)and(slp<=2826.65):
	sl=slp-(slp*0.075)
elif (slp>=2826.66)and(slp<=3751.05):
	sl=slp-(slp*0.15)
elif (slp>=3751.06)and(slp<=4664.68):
	sl=slp-(slp*0.225)
elif (slp>4664.68):
	sl=slp-(slp*0.275)
print("Salario liquido = R$",round(sl,2))