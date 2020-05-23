nota = float(input("Digite um numero:"))
opcao = input("Bonificacao? (S/N):")
acrescimo = 10/100

if(opcao == "S"):
	nf = nota + (nota * acrescimo)
else:
	nf = nota
print(float(nf))