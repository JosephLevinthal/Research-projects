x=int(input("idade: "))
y=float(input("imc: "))
print("Entradas:",x,"anos e IMC",y)

if(x<=0 and x>130 or y<=0):
	print("Dados invalidos")
else:
	if(y<22 and x<45):
		z="Baixo"
	elif(y>=22 and x<45):
		z="Medio"
	elif(y<22 and x>=45):
		z="Medio"
	elif(y>=22 and x>=45):
		z="Alto"
	print("Risco:",z)