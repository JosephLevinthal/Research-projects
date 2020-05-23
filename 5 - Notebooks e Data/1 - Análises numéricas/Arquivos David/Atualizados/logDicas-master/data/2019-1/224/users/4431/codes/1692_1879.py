x=float(input("Digite o numero de horas extras :"))
y=float(input("Digite o numero de horas de faltas: "))
h=x-(y*0.25)
if(h>400):
	print(x,"extras e",y,"de falta")
	print("R$ 500.0")
else:
	print(x,"extras e",y,"de falta")
	print("R$ 100.0")