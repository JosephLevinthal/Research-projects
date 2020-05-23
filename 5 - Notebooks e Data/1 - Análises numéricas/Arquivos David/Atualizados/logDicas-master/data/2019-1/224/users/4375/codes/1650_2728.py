p=float(input("digite o percurso em quilometros: "))
t=input("escolha um tipo de carro, A ou B: ")
if(t=="A".upper()):
	print(round(p*1/8,2))
else:
	print(round(p*1/12, 2))