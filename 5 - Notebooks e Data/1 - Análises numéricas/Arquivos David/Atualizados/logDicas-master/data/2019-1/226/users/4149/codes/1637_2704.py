nota=float(input("entre com a nota do aluno: "))
boni=input("vai receber a bonificao: S/N")

if(boni.upper()=="S"):

	notafin= nota+(nota*0.10)
	print(notafin)
	
else:
	print(nota)