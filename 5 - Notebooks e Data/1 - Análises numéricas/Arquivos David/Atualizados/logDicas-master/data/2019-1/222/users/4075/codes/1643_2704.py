nota= float(input("leia a nota do aluno: "))
opcao= input("informando se o aluno vai receber bonificacao (S/N)")
acrescimo=(nota*10)/100

if (opcao == "S"):
	x= nota+acrescimo
	
else:
	x= nota
	
print (x)
