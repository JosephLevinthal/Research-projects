nota = float(input("nota(0 a 10): "))
bonificacao = input("bonificacao(S ou N): ")
b = (nota) + (nota) * 10 / 100
if (bonificacao == "S"):
	p = b
else:
	p = nota
print(p)