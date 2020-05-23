i= int(input("digite sua idade: "))
im= float(input("digite o indice de massa corporal: "))
if (i>0)and(i<=130)and(im>0):
	if (im<22)and(i<45):
		z="Baixo"
		print("Entradas:",i,"anos e IMC",im)
		print("Risco:",z)
	elif (im<22)and(i>=45):
		z="Medio"
		print("Entradas:",i,"anos e IMC",im)
		print("Risco:",z)
	elif (im>=22)and(i<45):
		z="Medio"
		print("Entradas:",i,"anos e IMC",im)
		print("Risco:",z)
	elif (im>=22)and(i>=45):
		z="Alto"
		print("Entradas:",i,"anos e IMC",im)
		print("Risco:",z)
else:
	print("Entradas:",i,"anos e IMC",im)
	print("Dados invalidos")