x=int(input("Anos:"))
y=float(input("IMC:"))
print("Entradas:",x,"anos e IMC",y)
if((x<=0 or x>130) and (y<=0)):
	print("Dados invalidos")
else:
	if(x<45):
		if(y<22):
			print("Risco: Baixo")
		else:
			print("Risco: Medio")
	else:
		if(y<22):
			print("Risco: Medio")
		else:
			print("Risco: Alto")