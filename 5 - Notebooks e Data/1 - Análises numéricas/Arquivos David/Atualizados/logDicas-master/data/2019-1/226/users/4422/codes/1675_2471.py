ida = int(input("Qual a idade: "))
ind = float(input("Qual o IMC: "))
print("Entradas: ",ida, "anos e IMC", ind)

if(ida==0 or ida>=130 or ind<=0):
	print("Dados invalidos")
else:
	if(ida<45 and ind<22.0):
		print("Risco: Baixo")
	elif(ida<45 and ind>=22.0):
		print("Risco: Medio")
	elif(ida>=45 and ind<22.0):
		print("Risco: Medio")
	elif(ida>=45 and ind>=22.0):
		print("Risco: Alto")