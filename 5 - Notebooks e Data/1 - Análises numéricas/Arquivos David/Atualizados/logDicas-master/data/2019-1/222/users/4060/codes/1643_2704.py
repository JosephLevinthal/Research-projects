notas=float(input("nota do aluno: "))
boni=input("vai receber bonificacao?: ")
var=boni.upper()
if(var=="S"):
	men=notas+((10/100)*notas)
else:
	men=notas
print(men)	
	
	