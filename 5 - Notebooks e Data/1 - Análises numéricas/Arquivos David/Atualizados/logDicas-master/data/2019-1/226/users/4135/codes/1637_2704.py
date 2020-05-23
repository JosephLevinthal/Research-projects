nota = float(input("Digite a nota do aluno:"))
bonificacao = input ("bonificacao? S/N:")
if (bonificacao== "S"):
	nota = nota*1.1
print (round (nota,1))