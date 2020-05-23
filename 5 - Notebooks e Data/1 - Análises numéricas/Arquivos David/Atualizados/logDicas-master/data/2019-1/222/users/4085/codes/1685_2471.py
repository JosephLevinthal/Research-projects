i = int(input("escreva a idade da pessoa: "))
y = float(input("escreva o indice de massa corporal da pessoa: "))
print ("Entradas:", i, "anos e IMC", y)
if ((i <= 0) or (i > 130) or (y <= 0)):
	print ("Dados invalidos")
elif ((i < 45) and (y < 22.0)):
	print ("Risco: Baixo")
elif ((i >= 45) and (y < 22.0)):
	print ("Risco: Medio")
elif ((i < 45) and (y >= 22.0)):
	print ("Risco: Medio")
else:
	print ("Risco: Alto")
	