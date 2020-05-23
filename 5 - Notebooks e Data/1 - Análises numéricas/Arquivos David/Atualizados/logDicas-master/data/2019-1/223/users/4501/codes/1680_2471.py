a=int(input("idade: "))
b=float(input("massa corporal: "))
print("Entradas: ",a,"anos","e IMC",b)
if(a<45 and b<22):
	z="Baixo"
	print("Risco: ",z)
elif(a>=45 and b>=22.0):
	z="Medio"
	print("Risco: ",z)
elif(a<45 and b>=22):
	z="Medio"
	print("Risco: ",z)
elif(a>=45 and b>=22.0):
	z="Alto"
	print("Risco: ",z)
else:
	print("Dados invalidos")
	
