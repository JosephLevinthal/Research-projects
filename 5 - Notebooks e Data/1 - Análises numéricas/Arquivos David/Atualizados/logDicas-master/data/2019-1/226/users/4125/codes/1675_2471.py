idade = int(input("digite a idade: "))
imc = float(input("digite o imc: "))
x = "Entradas: "
y = "anos e IMC"

if (idade>0)and(imc>0):
	if(idade<45):
		if(imc<22):
			z = "Baixo"
		elif(imc>=22):
			z = "Medio"
	if (idade>=45):
		if(imc<22):
			z = "Medio"
		elif(imc>=22):
			z = "Alto"
	print(x,idade,y,imc)
	print("Risco: ",z)
elif(idade>=130)or(idade<=0)and(imc<=0):
	print(x,idade,y,imc)
	print("Dados invalidos")