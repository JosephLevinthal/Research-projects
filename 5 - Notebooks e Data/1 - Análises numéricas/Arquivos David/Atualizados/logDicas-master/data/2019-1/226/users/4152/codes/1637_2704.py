nota = float(input("Digite aqui a nota do aluno de 0 a 10: "))

msg = input("Digite se o aluno vai receber a bonificacao com S(sim) ou N(nao): ")

t1 = nota + ((10 * nota) / 100)

if (msg == "S"):
	nota = t1
else:
	nota
	
print(nota)