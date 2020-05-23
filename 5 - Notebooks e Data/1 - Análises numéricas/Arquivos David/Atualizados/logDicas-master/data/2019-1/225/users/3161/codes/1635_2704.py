nota= float(input("insira a nota do aluno: "))
b= input("vai receber bonificacao?")

if(b=="S"):
	total= nota + (nota*10/100)
else:
	total = nota
	
print(total)