nota = float(input("Digite sua nota: "))
boni = input("Bonificacao? (S/N): ")
Boni = (nota * 10)/100
if (boni.upper() == "S"):
	print(nota + Boni)
else:
	print(nota)
