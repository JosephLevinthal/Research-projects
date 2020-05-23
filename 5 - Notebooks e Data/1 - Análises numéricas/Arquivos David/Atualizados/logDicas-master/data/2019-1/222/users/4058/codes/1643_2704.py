n=float(input('digite a nota:'))
b=input('aluno vai receber bonificacao? (S/N)')
if (b.upper() == 'S'):
	a= n* (10/100)
	print(n+a)
else:
	print(n)