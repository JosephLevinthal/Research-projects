nota = float(input("Informe a nota do aluno: "))

bonificacao = input("recebe bonificacao (S/N) :")

if(bonificacao.upper())=="S":
   nota=nota+(nota*0.10)
else:
	nota=nota;
print(nota)	
   
