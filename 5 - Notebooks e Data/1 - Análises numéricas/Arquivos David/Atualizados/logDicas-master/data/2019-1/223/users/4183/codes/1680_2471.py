id = int(input("DIGITE ASUA IDADE: "))
imc = float(input("DIGITE SEU INDICE DE MASSA CORPORAL: "))

print("Entradas:", id, "anos e IMC", imc)

if (0 < id) and (id <= 130) and (0 < imc):
	
	if (imc < 22.0):
		if (id < 45):
			r = "Baixo"
		elif (id >= 45):
			r = "Medio"
	else:
		if (id < 45):
			r = "Medio"
		elif (id >= 45):
			r = "Alto"
		
	print("Risco:", r)

else: 
	print("Dados invalidos")
	
