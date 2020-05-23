x=float(input("Digite o salario liquido: "))
if(x<=1659.38):
	p=x*0.92
elif(x>=1659.39)and(x<=2765.67):
	p=x*0.91
elif(x>=2765.67)and(x<=5531.31):
	p=x*0.89
elif(x>5531.31):
	p=x-608.44

if(p<=1903.98):
	p=p-0
elif(p>=1903.99)and(p<=2826.65):
	p=p*(92.5/100)
elif(p>=2826.66)and(p<=3751.05):
	p=p*(85/100)
elif(p>=3751.06)and(p<=4664.68):
	p=p*(77.5/100)
else:
	p=p*(72.5/100)


print("Salario liquido = R$",(round(p,2)))	
	
	
	