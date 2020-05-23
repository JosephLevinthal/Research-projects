nota = float(input("digite a decepcao: "))
bonif = input("vai receber bonificacao? (S/N)")
acres = nota*10/100
if bonif == "S":
	print(float(nota + acres))
else:
	print(float(nota))
	
