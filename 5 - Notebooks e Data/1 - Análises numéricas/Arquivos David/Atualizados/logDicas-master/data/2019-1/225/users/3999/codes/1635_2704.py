nota=float(input("Nota do aluno:"))
bonificacao=input("Bonificacao? (S/N)")
if(bonificacao.upper()=="S"):
   total= nota + (nota*1/10)
else:
	total=nota
print(total)	
	