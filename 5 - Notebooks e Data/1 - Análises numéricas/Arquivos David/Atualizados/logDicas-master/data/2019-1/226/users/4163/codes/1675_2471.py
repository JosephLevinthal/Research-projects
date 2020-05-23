a = int(input("insira a idade: "))
b = float(input("insira o IMC: "))

print("Entradas:",a, "anos e IMC",b)

if ((a<45) and (b<22) and(a>0) and a>0and b>0):
	print("Risco: Baixo")
elif(a>=45 and b<22 and a<130) or (a<45 and b>=22 and a>0 and b>0):
	print("Medio")
elif(a>=45 and b>=22 and a<130 and b>0):
	print("Alto")
else:
	print("Dados invalidos")

	