a = int(input("idade: "))
b = float(input("IMC: "))
print("Entradas:",a,"anos e IMC", b)
if((a<=0 or a >130) or b <=0):
	print("Dados invalidos")
elif (a < 45 and b < 22):
	print( "Baixo")
elif( a >= 45 and b < 22):
	print("Medio")
elif(a < 45 and b >= 22):
	print("Medio")
elif(a >= 45 and b >= 22):
	print("Alto")
