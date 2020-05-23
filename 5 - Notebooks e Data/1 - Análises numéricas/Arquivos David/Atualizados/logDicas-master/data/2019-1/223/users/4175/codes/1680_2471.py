i = int(input())
im = float(input())

print("Entradas: ",i,"anos e IMC ",im)
if 0 <= i > 130 or im <= 0:
	print("Dados invalidos")
else:
	if i < 45 and im < 22:
		print("Risco: Baixo")
	elif i < 45 and im >= 22:
		print("Risco: Medio")
	elif i >= 45 and im < 22:
		print("Risco: Medio")
	elif i >= 45 and im >= 22:
		print("Risco: Alto")
	if 0 <= i > 130 or im <= 0:
		print("Dados invalidos")
