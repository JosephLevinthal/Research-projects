nota = float(input("Qual sua nota?"))
bonificacao = input("Vai receber bonificacao? (S/N)")

if(bonificacao.upper() == "S"):
	total = nota + nota/100*10
else:
	total = nota
print(total)