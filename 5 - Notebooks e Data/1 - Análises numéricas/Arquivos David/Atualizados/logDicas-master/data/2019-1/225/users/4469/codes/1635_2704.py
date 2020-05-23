nota = float(input("Entre com a nota do aluno: "))
bonificacao = input("Aluno recebe bonificacao? (S / N) ")

if(((bonificacao.upper() == "S") or (bonificacao.upper() == "N")) and ((nota >= 0.0) and (nota <= 10.0))):
	if(bonificacao.upper() == "S"):
		print(nota + ((nota * 10) / 100))
	else:
		print(nota)
else:
	print("Nota ou bonificacao invalidos")