i=int(input("digite a idade: "))
imc=float(input("digite o indice de massa corporal: "))
print("Entradas:", i, "anos e IMC", imc)
if(i<45) and (imc<22) and not(i<=0) and not(i>130) and not(imc<=0):
	print("Risco: Baixo")
elif(i<45) and (imc>=22) and not(i<=0) and not(i>130) and not(imc<=0):
	print("Risco: Medio")
elif(i>=45) and (imc<22) and not(i<=0) and not(i>130) and not(imc<=0):
	print("Risco: Medio")
elif(i>=45) and (imc>=22) and not(i<=0) and not(i>130) and not(imc<=0):
	print("Risco: Alto")
else:
	print("Dados invalidos")