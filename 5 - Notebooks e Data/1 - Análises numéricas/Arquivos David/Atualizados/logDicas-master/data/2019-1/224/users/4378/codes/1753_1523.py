qtd=int(input("Quantidade inicial de baloes: "))
qtdc=int(input("Quantidade C de novos baloes: "))
qtdd=int(input("Quantidade D de baloes destruidos: "))
x=qtdc-qtdd+qtd
if (x==200):
	print(0)
elif(x<200):
	print(x)
else:
	print(0)