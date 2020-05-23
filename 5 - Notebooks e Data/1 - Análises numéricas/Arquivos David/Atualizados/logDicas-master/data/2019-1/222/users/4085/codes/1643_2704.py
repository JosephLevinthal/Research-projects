nota = float(input("escreva a nota do aluno: "))
opcao = input("Recebe a bonificacao? (S/N): ")
if (opcao.upper()== "S"):
	nf = nota + 0.10 * nota
else: 
	nf = nota
	
print(nf)