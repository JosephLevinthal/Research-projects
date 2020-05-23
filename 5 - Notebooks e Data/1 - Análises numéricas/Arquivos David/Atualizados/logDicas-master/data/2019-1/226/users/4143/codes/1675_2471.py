a = int(input("Idade:"))
b = float(input("Indice de massa corporal:"))
print("Entradas: ", a, "anos e IMC ", b)
if ((a<=0)and(a>=130))or(b<=0):
	print("Dados invalidos")
elif (b<22.0)and(a<45):
	print("Risco: Baixo")
elif (b<22.0)and (a>=45):
	print("Risco: Medio")
elif (b>=22.0)and (a<45):
	print("Risco: Medio")
elif (b>=22.0)and(a>=45):
	print("Risco: Alto")