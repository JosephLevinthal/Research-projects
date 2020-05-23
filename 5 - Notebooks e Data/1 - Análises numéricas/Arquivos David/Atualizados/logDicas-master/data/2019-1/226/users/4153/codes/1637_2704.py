nota = float(input("Insira a nota do aluno: "))
bonificacao = input("Diga se o alura vai receber a bonificacao: (S/N)")

if(bonificacao.upper() == "S"):
	acrescimo = nota + (nota * 0.10)
else:
	acrescimo = nota

print(acrescimo)