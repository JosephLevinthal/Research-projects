salario=float(input())

if(salario<=1659.38):
	salario1=salario-(salario*0.08)
	if(salario1<=1903.98):
		print("Salario liquido = R$ ", round(salario1,2))
	elif(salario1>=1903.99 and salario1<=2826.65):
		salario2=salario1-(salario1*0.075)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=2826.66 and salario1<=3751.05):
		salario2=salario1-(salario1*0.15)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=3751.06 and salario1<=4664.68):
		salario2=salario1-(salario1*0.225)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>4664.68):
		salario2=salario1-(salario1*0.275)
		print("Salario liquido = R$ ", round(salario2,2))
elif(salario>=1659.39 and salario<=2765.66):
	salario1=salario-(salario*0.09)
	if(salario1<=1903.98):
		print("Salario liquido = R$ ", round(salario1,2))
	elif(salario1>=1903.99 and salario1<=2826.65):
		salario2=salario1-(salario1*0.075)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=2826.66 and salario1<=3751.05):
		salario2=salario1-(salario1*0.15)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=3751.06 and salario1<=4664.68):
		salario2=salario1-(salario1*0.225)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>4664.68):
		salario2=salario1-(salario1*0.275)
		print("Salario liquido = R$ ", round(salario2,2))
elif(salario>=2765.67 and salario<=5531.31):
	salario1=salario-(salario*0.11)
	if(salario1<=1903.98):
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=1903.99 and salario1<=2826.65):
		salario2=salario1-(salario1*0.075)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=2826.66 and salario1<=3751.05):
		salario2=salario1-(salario1*0.15)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=3751.06 and salario1<=4664.68):
		salario2=salario1-(salario1*0.225)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>4664.68):
		salario2=salario1-(salario1*0.275)
		print("Salario liquido = R$ ", round(salario2,2))
elif(salario>5531.31):
	salario1=salario-608.44
	if(salario1<=1903.98):
		print("Salario liquido = R$ ", round(salario1,2))
	elif(salario1>=1903.99 and salario1<=2826.65):
		salario2=salario1-(salario1*0.075)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=2826.66 and salario1<=3751.05):
		salario2=salario1-(salario1*0.15)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>=3751.06 and salario1<=4664.68):
		salario2=salario1-(salario1*0.225)
		print("Salario liquido = R$ ", round(salario2,2))
	elif(salario1>4664.68):
		salario2=salario1-(salario1*0.275)
		print("Salario liquido = R$ ", round(salario2,2))
	
