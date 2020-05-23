nota = float(input("digite a nota:"))
bonificacao = (input("tem bonificacao? "))
if (bonificacao == "S"):
	nota = (nota + (10/100)*nota)
else:
	nota = (nota)
print(nota)