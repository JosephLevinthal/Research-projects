age= int(input("qual a idade do individuo?"))
imc= float(input("qual o imc do individuo?"))

print("Entradas:", age, "anos e IMC", imc)

if(age<=0 or age>130 or imc<=0):
	print("Dados invalidos")
else:
	if(age<45 and imc<22.0):
		risco= "Baixo"
	elif (age>=45 and imc<22):
		risco="Medio"
	elif (age<45 and imc >=22):
		risco= "Medio"
	elif(age>=45 and imc>=22):
		risco= "Alto"
	print("Risco:",risco)