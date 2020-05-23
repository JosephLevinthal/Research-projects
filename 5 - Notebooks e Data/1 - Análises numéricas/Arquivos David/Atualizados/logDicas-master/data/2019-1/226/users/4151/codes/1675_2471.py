x=int(input("idade: "))
i=float(input("indice de massas corporal: "))
print("Entradas: ", x,"anos e IMC",i)
if(x<=0 or x>130 or i<=0):
	print("Dados invalidos")
elif(i<22.0)and(x<45):
	print("Risco: Baixo")
elif(i<22.0)and(x>=45):
	print("Risco: Medio")
elif(i>=22.0)and(x<45):
	print("Risco: Medio")
elif(i>=22.0)and(x>=45):
	print("Risco: Alto")
	
	